from elasticsearch import Elasticsearch
import json


class AlertHandler:
    elastic: Elasticsearch

    def __init__(self, elasticsearch: str, verify_certs: bool, api_key: str) -> None:
        """Initialize a class for handling alert documents.

        Args:
            elasticsearch (str): IP or URL of Elasticsearch instance.
            verify_certs (bool): Whether to verify certificates.
            api_key (str): API key for requests.
        """
        self.elastic = Elasticsearch(
            [elasticsearch],
            ssl_show_warn=False,
            verify_certs=verify_certs,
            api_key=api_key,
        )


class AlertFetcher(AlertHandler):

    def fetch(self, index: str, body: dict) -> list:
        """Return a list of documents from the resource.

        Args:
            index (str): Index where documents reside.
            body (str, optional): Json document containing the search parameters.

        Returns:
            list: List of document objects.
        """
        res = self.elastic.search(index=index, body=json.load(open(body)))
        return res["hits"]["hits"]


class AlertUploader(AlertHandler):

    def upload(self, index: str, documents: list) -> str:
        """Upload a list of documents to Elasticsearch.

        Args:
            index (str): Index to upload documents to.
            documents (list): List of documents to upload.

        Returns:
            str: Result of upload request.
        """
        for doc in documents:
            res = self.elastic.index(index=index, document=doc)
