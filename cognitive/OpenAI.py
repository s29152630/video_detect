import openai
from util.YamlLoader import YamlLoader
import util.Constant as const
from typing import List
from model.openai.Message import Message
from cognitive.OpenAIResultParser import OpenAIResultParser
from model.openai.OpenAIResult import OpenAIResult

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class OpenAI(metaclass=SingletonMeta):

    def __init__(self, open_ai_result_parser:OpenAIResultParser):
        self.open_ai_result_parser = open_ai_result_parser
        open_ai_config = YamlLoader().config[const.YAML_KEY_OPEN_AI]
        openai.api_type = open_ai_config[const.YAML_KEY_API_TYPE]
        openai.api_base = open_ai_config[const.YAML_KEY_API_BASE]
        openai.api_version = open_ai_config[const.YAML_KEY_API_VERSION]
        openai.api_key = open_ai_config[const.YAML_KEY_API_KEY]
        self.api_engine = open_ai_config[const.YAML_KEY_API_ENGINE]

    def call(self, messages: List[Message]) -> OpenAIResult:
        response = openai.ChatCompletion.create(
            engine=self.api_engine,
            messages=messages
        )
        open_ai_result = self.open_ai_result_parser.parse_result(response)

        return open_ai_result
        


