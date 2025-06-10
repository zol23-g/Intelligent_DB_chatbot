from fastapi import APIRouter
from app.services.data_loader_service import fetch_all_mysql_tables
from app.services.embedding_service import create_document_embeddings, model
from app.services.elasticsearch_service import index_documents, semantic_search

router = APIRouter()

@router.post("/build-index")
def build_index():
    data = fetch_all_mysql_tables()
    docs = create_document_embeddings(data)
    index_documents(docs)
    return {"message": "Index built successfully", "total_docs": len(docs)}

@router.get("/search")
def search_query(q: str):
    results = semantic_search(q, model)
    return {"results": results}
