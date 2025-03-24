import requests
from typing import Dict, Any
from config import VECTOR_MICROSERVICE_URL

def add_document(collection_name: str, document: Dict[str, Any]) -> Dict:
    """
    Sends a document to the ChromaDB microservice for storage.
    :param collection_name: The name of the collection in ChromaDB.
    :param document: A dictionary containing 'id', 'content', and 'metadata'.
    :return: Response from the ChromaDB microservice.
    """
    payload = {"collection_name": collection_name, "document": document}
    response = requests.post(f"{VECTOR_MICROSERVICE_URL}/add_document/", json=payload)
    return response.json()



def query_documents(collection_name: str, query_text: str, top_k: int = 5) -> Dict:
    """
    Queries the ChromaDB microservice to retrieve relevant documents.
    :param collection_name: The collection to query.
    :param query_text: The search query.
    :param top_k: Number of results to return.
    :return: Response from ChromaDB with similar documents.
    """
    payload = {"collection_name": collection_name, "query_text": query_text, "top_k": top_k}
    response = requests.post(f"{VECTOR_MICROSERVICE_URL}/query/", json=payload)
    return response.json()
