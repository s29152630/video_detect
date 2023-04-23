from model.bus.Event import Event

class DataProcessEvent(Event):

    def __init__(self, flow_name: str):
        super().__init__(flow_name)

    @property
    def video_path(self) -> str:
        return self.__video_path
    
    @video_path.setter
    def video_path(self, value:str):
        self.__video_path = value

