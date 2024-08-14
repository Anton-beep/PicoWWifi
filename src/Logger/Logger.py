from MyTime.MyTime import MyTime


class Logger:
    @staticmethod
    def _prefix_logger(data_type: str, time: MyTime) -> str:
        return f"{data_type} [{str(time)}]: "

    @staticmethod
    def info(msg) -> None:
        print(Logger._prefix_logger("INFO", MyTime.now()) + str(msg))

    @staticmethod
    def warning(msg) -> None:
        print(Logger._prefix_logger("WARNING", MyTime.now()) + str(msg))

    @staticmethod
    def error(msg) -> None:
        print(Logger._prefix_logger("ERROR", MyTime.now()) + str(msg))
