from model.image.ResultDetail import ResultDetail
from model.image.ErrorDetail import ErrorDetail
from model.image.ContentResult import ContentResult
from typing import List


class ImageAnalysisResult():

    def __init__(self, result_detail: ResultDetail, error_detail: ErrorDetail, content_results: List[ContentResult]):
        self.result_detail = result_detail
        self.error_detail = error_detail
        self.content_results = content_results

    @property
    def result_detail(self) -> ResultDetail:
        return self.__result_detail

    @result_detail.setter
    def result_detail(self, value: ResultDetail):
        self.__result_detail = value

    @property
    def error_detail(self) -> ErrorDetail:
        return self.__error_detail

    @error_detail.setter
    def error_detail(self, value: ErrorDetail) -> ErrorDetail:
        self.__error_detail = value

    @property
    def content_results(self) -> List[ContentResult]:
        return self.__content_results
    
    @content_results.setter
    def content_results(self, value: List[ContentResult]):
        self.__content_results = value