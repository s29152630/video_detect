

class Event():

    def __init__(self, flow_name: str):
        self.__flow_name = flow_name

    @property
    def flow_name(self) -> str:
        return self.__flow_name

    @flow_name.setter
    def flow_name(self, value: str):
        self.__flow_name = value
