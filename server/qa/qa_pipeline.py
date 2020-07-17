from haystack import Finder
from haystack.reader.farm import FARMReader
from haystack.database.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever

from .utils import *


class QAPipeline:
    def __init__(self):
        self.document_store = ElasticsearchDocumentStore(
            host="localhost", username="", password="", index="document")
        self.retriever = ElasticsearchRetriever(
            document_store=self.document_store)
        self.reader = FARMReader(
            model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
        self.finder = Finder(self.reader, self.retriever)

    def add_to_datastore_from_remote(self, data_url):
        return {'status': 'Not Implemented'}

    def add_to_datastore_local(self, data_path):
        json_data = read_json_data(data_path)
        es_data = create_data_dicts(json_data)
        self.document_store.write(es_data)
        return {'status': 'Added To Datastore'}

    def answer(self, question, top_k_options=10, top_k_answers=3):
        prediction = self.finder.get_answers(
            question=question, top_k_retriever=top_k_options, top_k_reader=top_k_answers)
        results = extract_info_from_predictions(prediction)
        return results
