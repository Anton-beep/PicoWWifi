import time

import urequests

from Logger.Logger import Logger


class MyRequests:
    REPEAT_COOLDOWN = 5

    @staticmethod
    async def _basic_request(method: str, url: str, **kwargs):
        while True:
            try:
                return getattr(urequests, method)(url, **kwargs)
            except Exception as ex:
                Logger.error(
                    f"failed {method} request: URL: {url} EXCEPTION: {ex} KWARGS: {kwargs}"
                )
                time.sleep(MyRequests.REPEAT_COOLDOWN)

    @staticmethod
    async def get(url: str, **kwargs):
        return await MyRequests._basic_request("get", url, **kwargs)

    @staticmethod
    async def post(url: str, **kwargs):
        return await MyRequests._basic_request("post", url, **kwargs)
