from MyDataClass.MyDataClass import MyDataClass


class BotCommandScopeChat(MyDataClass):
    def __init__(self, type: str, chat_id: str):
        self.type = type
        self.chat_id = chat_id
