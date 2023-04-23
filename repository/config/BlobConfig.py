from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


class BlobConfig:

    def __init__(self, a) -> None:
        pass


class BlobConfigDev(BlobConfig):

    def __init__(self, connect_str) -> None:
        super().__init__(connect_str)
        try:
            # self.blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            self.blob_service_client = connect_str
        except Exception as ex:
            print('Exception:')
            print(ex)

    def print(self):
        print(self.blob_service_client)


class BlobConfigNonDev(BlobConfig):

    def __init__(self, storage_account_name) -> None:
        try:
            account_url = "https://{}.blob.core.windows.net".format(
                storage_account_name)
            default_credential = DefaultAzureCredential()
            self.blob_service_client = BlobServiceClient(
                account_url, credential=default_credential)

        except Exception as ex:
            print('Exception:')
            print(ex)
