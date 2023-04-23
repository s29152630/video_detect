from model.bus.Event import Event

class DataAnalysisEvent(Event):

    def __init__(self, flow_name: str):
        super().__init__(flow_name)

    @property
    def frame_directory(self) -> str:
        return self.__frame_directory
    
    @frame_directory.setter
    def frame_directory(self, value:str):
        self.__frame_directory = value