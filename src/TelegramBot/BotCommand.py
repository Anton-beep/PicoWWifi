from MyDataClass.MyDataClass import MyDataClass


class BotCommand(MyDataClass):
    def __init__(self, command: str, description: str):
        self.command = command
        self.description = description
