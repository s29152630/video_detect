from util.YamlLoader import YamlLoader
import util.Constant as const
import azure.ai.vision as visionsdk
from cognitive.ImageAnalysisResultParser import ImageAnalysisResultParser
from model.image.ImageAnalysisResult import ImageAnalysisResult


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# need to implement read image from blob
class ImageAnalysis(metaclass=SingletonMeta):

    def __init__(self, image_analysis_result_parser: ImageAnalysisResultParser):
        self.image_analysis_result_parser = image_analysis_result_parser
        image_analysis_config = YamlLoader(
        ).config[const.YAML_KEY_IMAGE_ANALYSIS]
        vision_key = image_analysis_config[const.YAML_KEY_VISION_KEY]
        vision_endpoint = image_analysis_config[const.YAML_KEY_VISION_ENDPOINT]
        self.service_options = visionsdk.VisionServiceOptions(
            vision_endpoint, vision_key)

    def call_dense_caption(self) -> ImageAnalysisResult:
        analysis_options = visionsdk.ImageAnalysisOptions()
        analysis_options.features = (
            visionsdk.ImageAnalysisFeature.DENSE_CAPTIONS
        )
        analysis_options.language = "en"
        analysis_options.model_version = "latest"
        analysis_options.gender_neutral_caption = False

        image_analyzer = visionsdk.ImageAnalyzer(
            self.service_options, vision_source, analysis_options)
        result = image_analyzer.analyze()
        image_analysis_result = self.image_analysis_result_parser.parse_result(result)
        return image_analysis_result
