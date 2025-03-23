from fastapi import FastAPI, HTTPException
import chromadb

from models import AddDocumentRequestData, QueryDocumentRequestData

app = FastAPI()

chroma_client = chromadb.PersistentClient(path="./data/chroma")

@app.post("/add_document/")
def add_document(data: AddDocumentRequestData):
    """ Adds a document vector to ChromaDB """
    try:
        collection = chroma_client.get_or_create_collection(name=data.collection_name)
        collection.add(
            documents=[data.document.content],
            metadatas=[data.document.metadata],
            ids=[data.document.id]
        )
        return {"message": "Document added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/")
def query_documents(data: QueryDocumentRequestData):
    """ Queries similar vectors from ChromaDB """
    try:
        collection = chroma_client.get_or_create_collection(name=data.collection_name)
        results = collection.query(query_texts=[data.query_text], n_results=data.top_k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

