from repository.config.BlobConfig import BlobConfig


class BlobManager():

    def __init__(self, blob_config: BlobConfig) -> None:
        self.blob_config = blob_config