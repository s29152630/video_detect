

class ErrorDetail():

    def __init__(self, reason: str, error_code: str, message: str):
        self.reason = reason
        self.error_code = error_code
        self.message = message

    @property
    def reason(self) -> str:
        return self.__reason

    @reason.setter
    def reason(self, value: str):
        self.__reason = value

    @property
    def error_code(self) -> str:
        return self.__error_code

    @error_code.setter
    def error_code(self, value: str):
        self.__error_code = value

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value
