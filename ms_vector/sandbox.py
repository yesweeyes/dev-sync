from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import OllamaEmbeddings

app = FastAPI()

# Initialize Ollama Embeddings
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")

class TextRequest(BaseModel):
    text: str

@app.post("/embed")
def embed_text(request: TextRequest):
    try:
        embedding = embedding_model.embed_query(request.text)
        return {"embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "Ollama Embeddings Sandbox is running!"}
