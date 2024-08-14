import network
import time

from Logger.Logger import Logger


class Wlan:
    MAX_TIMEOUT_CONNECT = 10

    def __init__(self, ssid: str, password: str) -> None:
        self.ssid = ssid
        self.password = password

        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect_to_wifi(self) -> bool:
        self.wlan.connect(self.ssid, self.password)
        for elapsed in range(Wlan.MAX_TIMEOUT_CONNECT):
            Logger.info(network.STAT_NO_AP_FOUND)
            Logger.info(f"trying to connect to wifi, status: {self.wlan.status()}")
            if self.wlan.isconnected():
                break

            time.sleep(1)

        if self.wlan.isconnected():
            return True
        return False
