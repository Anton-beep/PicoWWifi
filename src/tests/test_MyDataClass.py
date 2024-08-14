from MyDataClass.MyDataClass import MyDataClass


class TestDataClass(MyDataClass):
    def __init__(self, bib: str, bob: str) -> None:
        self.bib = bib
        self.bob = bob


def test_MyDataClass() -> None:
    test_data = TestDataClass("bib", "bob")
    assert str(test_data) == "{'bib': 'bib', 'bob': 'bob'}"


test_MyDataClass()
