class MyDataClass:
    def get_dict(self):
        d = dict()

        for key in dir(self):
            if not callable(getattr(self, key)) and key[0] != "_":
                d[key] = getattr(self, key)

        return d

    def __str__(self) -> str:
        return str(self.get_dict())
