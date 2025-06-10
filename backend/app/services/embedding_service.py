from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from app.config import settings

model = SentenceTransformer(settings.EMBEDDING_MODEL)

def create_document_embeddings(data: dict):
    documents = []
    for table, df in data.items():
        for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Embedding {table}"):
            text = f"{table}: " + ", ".join([f"{col}={row[col]}" for col in df.columns])
            embedding = model.encode(text)
            documents.append({
                "table": table,
                "text": text,
                "embedding": embedding.tolist()
            })
    return documents
