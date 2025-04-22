from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GEMINI_API_KEY

def generate_user_story_helper(summary: str, user_prompt: str):
    # Set up the model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-001",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key=GEMINI_API_KEY,
    )

    # Example structure to guide the model
    example_output = """
[
  {
      "summary": "User Registration",
      "description": "As a new user, I want to register an account so that I can access the platform.",
      "Acceptance Criteria": "The user should be able to enter their details (name, email, password).",
      "issueType": "Story",
      "labels": ["authentication", "user-management"],
      "storyPoints": 3,
      "Priority": "High"
  }
]
    """

    # System message (instruction)
    system_message = f"""
You are an AI that generates software development user stories.
Output must be a valid, JSON-parsable array of user stories with this structure:
{example_output}
Do not include explanations, markdown, or backticks — just return the array.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", "{system_message}"),
        ("human", "{summary}"),
        ("human", "{user_prompt}")
    ])

    # Chain and response
    chain = prompt | llm
    response = chain.invoke({
        "system_message": system_message,
        "summary": summary,
        "user_prompt": user_prompt,
    })

    response = response.content.strip().lstrip("```json").rstrip("```")
    
    try:
        return response
    except Exception as e:
        raise ValueError(f"Failed to parse model output as JSON: {e}\nRaw Output:\n{response.content}")
