import yaml

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class YamlLoader(metaclass=SingletonMeta):

    def __init__(self) :
        self.config = self.load('config.yaml')

    def load(self, path: str) -> dict:
        with open(path, 'r') as stream:
            try:
                d = yaml.safe_load(stream)
                return d
            except yaml.YAMLError as e:
                print(e)