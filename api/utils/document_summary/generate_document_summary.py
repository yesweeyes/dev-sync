from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from config import GEMINI_API_KEY


def generate_document_summary(documet_content: str) -> str:
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GEMINI_API_KEY,
    # other params...
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a software requirements gathering specialist. Presented with a requirement document, return a summary of requirements.",
            ),
            ("assistant", "{document_content}"),
        ]
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "document_content": documet_content,
        }
    )
    return response.content