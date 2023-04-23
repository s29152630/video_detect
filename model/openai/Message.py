

class Message():

    def __init__(self, role: str, content: str) -> None:
        self.__role = role
        self.__content = content

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, value: str):
        self.__role = value

    @property
    def content(self) -> str:
        return self.__content

    @role.setter
    def content(self, value: str):
        self.__content = value
