from abc import abstractmethod
from repository.blob.BlobManager import BlobManager
from opencv.VideoProcessor import VideoProcessor
from typing import List


# template pattern
class DataProcessFlow():

    def execute(self):
        self.read_data()
        self.process_data()
        self.save_result()

    @abstractmethod
    def read_data(self): pass

    @abstractmethod
    def process_data(self): pass

    @abstractmethod
    def save_result(self): pass

# need to implement detail
class LocalProcessFlow(DataProcessFlow):

    def __init__(self, blob_manager: BlobManager, video_processor: VideoProcessor):
        super().__init__()
        self.blob_manager = blob_manager
        self.video_processor = video_processor

    def read_data(self) -> any:
        self.blob_manager

    def process_data(self) -> List[any]:
        self.video_processor

    def save_result(self) -> bool:
        self.blob_manager
