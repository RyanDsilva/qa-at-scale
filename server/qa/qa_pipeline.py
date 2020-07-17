from haystack import Finder
from haystack.reader.farm import FARMReader
from haystack.database.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever


class QAPipeline:
    pass


document_store = ElasticsearchDocumentStore(
    host="localhost", username="", password="", index="document")

# TODO: Read Data and Write to ES

retriever = ElasticsearchRetriever(document_store=document_store)
reader = FARMReader(
    model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
finder = Finder(reader, retriever)

prediction = finder.get_answers(
    question="What are the ways to perform Named Entity Recognition?", top_k_retriever=15, top_k_reader=3)
