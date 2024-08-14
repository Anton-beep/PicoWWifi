from Logger.Logger import Logger
from Wlan.Wlan import Wlan
from ConfigReader.ConfigReader import ConfigReader


def main() -> None:
    Logger.info("+++START+++")

    cfg = ConfigReader()
    cfg.read("config.cfg")

    Logger.info(f"{cfg['SSID']} {cfg['SSID_PASSWORD']}")
    wlan = Wlan(cfg["SSID"], cfg["SSID_PASSWORD"])
    if not wlan.connect_to_wifi():
        Logger.error("failed to connect to wifi")
        return

    Logger.info("connected to wifi")


if __name__ == "__main__":
    main()
