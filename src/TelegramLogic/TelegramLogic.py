import asyncio
import time

import machine

from Logger.Logger import Logger
from TelegramBot.BotCommand import BotCommand
from TelegramBot.BotCommandScopeChat import BotCommandScopeChat
from TelegramBot.TelegramBot import TelegramBot


class TelegramLogic:
    def __init__(self, tg_bot: TelegramBot, good_chats: str) -> None:
        self.tg_bot = tg_bot
        self.commands = [
            BotCommand("ping", "ping pong, bot availability test"),
            BotCommand("turn_on", "turn on"),
        ]
        self.good_chats = good_chats.split(",")

        for chat in self.good_chats:
            asyncio.create_task(
                self.tg_bot.set_my_commands(
                    self.commands, BotCommandScopeChat("chat", chat)
                )
            )

        # trigger function must start with is_ and return bool
        # action funcrion must start with act_

        # self.triggers stores the order
        self.triggers = [
            self.is_unwanted_user,  # must be first
            self.is_ping,
            self.is_turn_on,
        ]

        self.triggers.append(self.is_nothing_to_send)

        # self.trigger_action stores actions with triggers
        self.trigger_action = {
            self.is_unwanted_user: self.act_ignore,
            self.is_ping: self.act_pong,
            self.is_turn_on: self.act_turn_on,
            self.is_nothing_to_send: self.act_unknown_command,
        }

        if len(self.triggers) != len(self.trigger_action):
            raise Exception("len of self.triggers != len of self.trigger_action")

    async def is_turn_on(self, update: dict) -> bool:
        return self.get_safely_message_text(update) == "/turn_on"

    async def act_turn_on(self, update: dict) -> None:
        chat_id = self.get_safely_chat_id(update)
        if not chat_id:
            return

        turnOnPin = machine.Pin(15, machine.Pin.OUT)

        await self.tg_bot.send_text_message("pressing the button...", chat_id)

        turnOnPin.on()
        time.sleep(5)
        turnOnPin.off()

        await self.tg_bot.send_text_message("the button was pressed", chat_id)

    async def is_nothing_to_send(self, update: dict) -> bool:
        return True

    async def act_unknown_command(self, update: dict) -> None:
        chat_id = self.get_safely_chat_id(update)
        if not chat_id:
            return

        await self.tg_bot.send_text_message("unknown command", chat_id)

    async def is_unwanted_user(self, update: dict) -> bool:
        return str(self.get_safely_chat_id(update)) not in self.good_chats

    async def act_ignore(self, update: dict) -> None:
        Logger.warning(f"ignored: {update}")

    def get_safely_chat_id(self, update: dict):
        """chat_id if success, None on failure"""
        if (
            "message" in update
            and "chat" in update["message"]
            and "id" in update["message"]["chat"]
        ):
            return update["message"]["chat"]["id"]

    def get_safely_message_text(self, update: dict):
        if "message" in update and "text" in update["message"]:
            return update["message"]["text"]

    async def is_ping(self, update: dict) -> bool:
        return self.get_safely_message_text(update) == "/ping"

    async def act_pong(self, update: dict) -> None:
        chat_id = self.get_safely_chat_id(update)
        if not chat_id:
            return

        await self.tg_bot.send_text_message("pong", chat_id)

    def run(self) -> None:
        offset = None

        while True:
            updates = asyncio.run(self.tg_bot.get_updates(offset, 3))

            if "result" not in updates:
                Logger.error(f"result not in updates: {updates}")
                continue

            updates = updates["result"]

            for update in updates:
                Logger.info(f"update: {update}")

                offset = update["update_id"] + 1

                for trigger in self.triggers:
                    if asyncio.run(trigger(update)):
                        asyncio.create_task(self.trigger_action[trigger](update))
                        break
