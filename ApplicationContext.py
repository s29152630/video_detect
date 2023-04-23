from util.YamlLoader import YamlLoader 
from repository.config.BlobConfigSimpleFactory import BlobConfigSimpleFactory
from repository.blob.BlobManager import BlobManager
from opencv.VideoProcessor import VideoProcessor
from cognitive.ImageAnalysis import ImageAnalysis
from cognitive.ImageAnalysisResultParser import ImageAnalysisResultParser
from cognitive.OpenAI import OpenAI
from cognitive.OpenAIResultParser import OpenAIResultParser
from workflow.DataProcessFlow import LocalProcessFlow
from workflow.DataAnalysisFlow import LocalAnalysisFlow
import util.Constant as const 

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class ApplicationContext(metaclass=SingletonMeta):

    def init(self): 
        self.config = YamlLoader().config
        self.blob_configs = BlobConfigSimpleFactory().create_blob_configs()
        self.blob_managers = dict(map(lambda e: (e[0], BlobManager(e[1])), self.blob_configs.items()))
        self.image_analysis_result_parser = ImageAnalysisResultParser()
        self.image_analysis = ImageAnalysis(self.image_analysis_result_parser)
        self.open_ai_result_parser = OpenAIResultParser()
        self.open_ai = OpenAI(self.open_ai_result_parser)
        self.video_processor = VideoProcessor()
        self.local_process_flow = LocalProcessFlow(self.blob_manager, self.video_processor)
        self.local_analysis_flow = LocalAnalysisFlow(self.blob_manager, self.image_analysis, self.open_ai)
        self.process_flows = {
            const.DATA_PROCESS_FLOW_LOCAL: self.local_process_flow
        }
        self.analysis_flows = {
            const.DATA_ANALYSIS_FLOW_LOCAL: self.local_analysis_flow
        }




container = ApplicationContext()
container.init()
print(container.config)
container.blob_configs
container.blob_managers

print('hhh')
