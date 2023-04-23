from abc import abstractmethod
from repository.blob.BlobManager import BlobManager
from cognitive.ImageAnalysis import ImageAnalysis
from cognitive.OpenAI import OpenAI

# template pattern
class DataAnalysisFlow():

    def execute(self):
        self.read_data()
        self.analyze_data()
        self.save_result()

    @abstractmethod
    def read_data(self): pass

    @abstractmethod
    def analyze_data(self): pass

    @abstractmethod
    def save_result(self): pass

# need to implement read image from blob
class LocalAnalysisFlow(DataAnalysisFlow):

    def __init__(self, blob_manager: BlobManager, image_analysis: ImageAnalysis, open_ai: OpenAI):
        super().__init__()
        self.blob_manager = blob_manager
        self.image_analysis = image_analysis
        self.open_ai = open_ai

    def read_data(self) -> any:
        self.blob_manager

    def analyze_data(self):
        self.image_analysis
        self.open_ai

    def save_result(self) -> bool:
        self.blob_manager
