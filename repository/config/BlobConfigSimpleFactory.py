from util.YamlLoader import YamlLoader
from BlobConfig import BlobConfig, BlobConfigDev, BlobConfigNonDev
import util.Constant as const
from typing import Dict


class BlobConfigSimpleFactory:

    def create_blob_configs(self) -> Dict[str, BlobConfig]:
        config = YamlLoader().config
        profile = config[const.profile]
        if profile == const.PROFILE_DEV:
            blob_configs = dict(map(lambda e: (e[const.YAML_KEY_NAME], BlobConfigDev(
                e[const.YAML_KEY_CONNECTION_STRING])), config[const.YAML_KEY_BLOB][const.YAML_KEY_STORAGE_ACCOUNT]))
        elif profile == const.PROFILE_UAT:
            blob_configs = dict(map(lambda e: (e[const.YAML_KEY_NAME], BlobConfigNonDev(
                e[const.YAML_KEY_NAME])), config[const.YAML_KEY_BLOB][const.YAML_KEY_STORAGE_ACCOUNT]))
        elif profile == const.PROFILE_PROD:
            blob_configs = dict(map(lambda e: (e[const.YAML_KEY_NAME], BlobConfigNonDev(
                e[const.YAML_KEY_NAME])), config[const.YAML_KEY_BLOB][const.YAML_KEY_STORAGE_ACCOUNT]))
        else:
            blob_configs = dict(map(lambda e: (e[const.YAML_KEY_NAME], BlobConfigDev(
                e[const.YAML_KEY_CONNECTION_STRING])), config[const.YAML_KEY_BLOB][const.YAML_KEY_STORAGE_ACCOUNT]))

        return blob_configs
