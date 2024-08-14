import json
import time

import urequests

from Logger.Logger import Logger
from MyRequests.MyRequests import MyRequests
from TelegramBot.BotCommand import BotCommand
from TelegramBot.BotCommandScopeChat import BotCommandScopeChat


class TelegramBot:
    BASE_URL = "https://api.telegram.org/bot"

    def __init__(self, token: str) -> None:
        self.token = token

    async def get_updates(self, offset=None, timeout: int = 0) -> dict:
        url = f"{self.BASE_URL}{self.token}/getUpdates"

        params = {"timeout": timeout}
        if offset:
            params["offset"] = offset

        return (await MyRequests.get(url, json=params)).json()

    async def set_my_commands(
        self, commands: list[BotCommand], scope: BotCommandScopeChat
    ) -> dict:
        url = f"{self.BASE_URL}{self.token}/setMyCommands"

        params = {
            "commands": json.dumps([command.get_dict() for command in commands]),
            "scope": json.dumps(scope.get_dict()),
        }

        return (await MyRequests.post(url, json=params)).json()

    async def send_text_message(self, msg: str, chat_id: int, parse_mode=None) -> dict:
        url = f"{self.BASE_URL}{self.token}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": msg,
        }

        if parse_mode:
            params["parse_mode"] = parse_mode

        return (await MyRequests.post(url, json=params)).json()
