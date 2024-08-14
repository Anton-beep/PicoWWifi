from ConfigReader.ConfigReader import ConfigReader
from Logger.Logger import Logger
from MyRequests.MyRequests import MyRequests
from TelegramBot.TelegramBot import TelegramBot
from TelegramLogic.TelegramLogic import TelegramLogic
from Wlan.Wlan import Wlan


def main() -> None:
    Logger.info("+++START+++")

    cfg = ConfigReader()
    cfg.read("config.cfg")

    wlan = Wlan(cfg["SSID"], cfg["SSID_PASSWORD"])
    if not wlan.connect_to_wifi():
        Logger.error("failed to connect to wifi")
        return

    Logger.info("connected to wifi")

    TelegramLogic(TelegramBot(cfg["TG_TOKEN"]), cfg["GOOD_CHATS"]).run()


if __name__ == "__main__":
    main()
