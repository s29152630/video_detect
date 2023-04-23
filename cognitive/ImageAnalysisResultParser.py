import azure.ai.vision as visionsdk
from model.image.ImageAnalysisResult import ImageAnalysisResult
from model.image.ResultDetail import ResultDetail
from model.image.ErrorDetail import ErrorDetail
from model.image.ContentResult import ContentResult
from model.image.DenseCaptionResult import DenseCaptionResult

# Remember check visionsdk return maybe no need so much model
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ImageAnalysisResultParser(metaclass=SingletonMeta):

    def __init__(self) -> None:
        pass

    def parse_result(self, result: any) -> ImageAnalysisResult:

        image_analysis_result = ImageAnalysisResult()
        if result.reason == visionsdk.ImageAnalysisResultReason.ANALYZED:
            if result.dense_captions is not None:
                dense_caption_results = map(lambda e: DenseCaptionResult(
                    e.content, e.bunding_box, e.confidence), result.dense_captions)
                image_analysis_result.content_results = dense_caption_results

            result_details = visionsdk.ImageAnalysisResultDetails.from_result(
                result)
            image_analysis_result.result_detail = result_details

        elif result.reason == visionsdk.ImageAnalysisResultReason.ERROR:
            error_details = visionsdk.ImageAnalysisErrorDetails.from_result(
                result)
            image_analysis_result.error_detail = error_details

        return image_analysis_result
