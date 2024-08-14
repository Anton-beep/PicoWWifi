class ConfigReader:
    def read(self, path: str):
        with open(path) as f:
            for line in f.readlines():
                key, val = line.split("=")
                setattr(self, key, val.rstrip())

    def __getitem__(self, key: str):
        return getattr(self, key)
