

class OpenAIResult():

    def __init__(self, content: str) -> None:
        self.__content = content

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str):
        self.__content = value
