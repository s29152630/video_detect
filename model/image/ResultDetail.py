

class ResultDetail():

    def __init__(self, image_id: str, result_id: str, connection_url: str, json_result: str):
        self.image_id = image_id
        self.result_id = result_id
        self.connection_url = connection_url
        self.json_result = json_result

    @property
    def image_id(self) -> str:
        return self.__image_id

    @image_id.setter
    def image_id(self, value: str):
        self.__image_id = value

    @property
    def result_id(self) -> str:
        return self.__result_id

    @result_id.setter
    def result_id(self, value: str):
        self.__result_id = value

    @property
    def connection_url(self) -> str:
        return self.__connection_url

    @connection_url.setter
    def connection_url(self, value: str):
        self.__connection_url = value

    @property
    def json_result(self) -> str:
        return self.__json_result

    @json_result.setter
    def json_result(self, value: str):
        self.__json_result = value
