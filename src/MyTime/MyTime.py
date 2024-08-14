import time


class MyTime:
    @staticmethod
    def now():
        return MyTime(*time.localtime())

    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        week_day: int = 0,
        year_day: int = 0,
    ):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.week_day = week_day
        self.year_day = year_day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}T{self.hour}:{self.minute}:{self.second}"
