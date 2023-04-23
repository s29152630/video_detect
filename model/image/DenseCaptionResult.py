import ContentResult


class DenseCaptionResult(ContentResult):

    def __init__(self, content: str, bounding_box: str, confidence: int):
        self.content = content
        self.bounding_box = bounding_box
        self.confidence = confidence

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str):
        self.__content = value

    @property
    def bounding_box(self) -> str:
        return self.__bounding_box

    @bounding_box.setter
    def bounding_box(self, value: str):
        self.__bounding_box = value

    @property
    def confidence(self) -> int:
        return self.__confidence

    @confidence.setter
    def confidence(self, value: int):
        self.__confidence = value
