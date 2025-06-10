from app.config import settings
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import numpy as np

# Setup
es = Elasticsearch(
    ["http://localhost:9200"],  
    basic_auth=("elastic", "password") 
)
model = SentenceTransformer("all-MiniLM-L6-v2")
INDEX_NAME = "classicmodels_semantic"

def query_semantic_elasticsearch(query: str, top_k: int = 10) -> list[str]:
    embedding = model.encode(query).tolist()

    body = {
        "size": top_k,
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": embedding}
                }
            }
        }
    }

    response = es.search(index=INDEX_NAME, body=body)
    hits = response.get("hits", {}).get("hits", [])

    return [f"{hit['_source']['text']} (score: {hit['_score']:.2f})" for hit in hits]
