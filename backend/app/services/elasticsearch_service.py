from elasticsearch import Elasticsearch
from app.config import settings

es = Elasticsearch(
    ["http://localhost:9200"],  # or your Elasticsearch URL
    basic_auth=("elastic", "password")  # provide valid credentials
)
INDEX_NAME = "classicmodels_semantic"

def index_documents(documents):
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
    es.indices.create(index=INDEX_NAME)

    for doc in documents:
        es.index(index=INDEX_NAME, body=doc)

def semantic_search(query: str, model, top_k: int = 5):
    query_vec = model.encode(query)

    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_vec.tolist()}
            }
        }
    }

    response = es.search(index=INDEX_NAME, query=script_query, size=top_k)
    return [(hit["_source"]["text"], hit["_score"]) for hit in response["hits"]["hits"]]
