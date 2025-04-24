import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from app.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
    api_version="v1"
)

# Prompt template for code review
code_review_prompt = PromptTemplate.from_template(
    """You are a senior software engineer reviewing a code submission.

Please provide a detailed HTML-formatted review of the following code:
- Highlight bugs or potential issues.
- Suggest improvements (readability, performance, best practices).
- Add missing documentation if needed.
- Use <pre><code> for code blocks.
- Format with proper headings and bullet points.
- Strictly adhere to the user prompt given below, extend or overule previous conditions.

User Prompt:
```{user_prompt}```

Code:
```{code}```
"""
)

def generate_code_review_html(code: str, user_prompt: str) -> str:
    # Format the prompt
    prompt = code_review_prompt.format(code=code, user_prompt=user_prompt)

    # Get Gemini response
    response = llm.invoke(prompt)
    html_body = response.content if hasattr(response, "content") else str(response)

    # Wrap it inside a basic HTML structure
    html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Code Review</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 2rem; }}
        code {{ background-color: #f4f4f4; padding: 0.2rem 0.4rem; border-radius: 4px; }}
        pre {{ background-color: #f9f9f9; padding: 1rem; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>Code Review Report</h1>
    {html_body}
</body>
</html>
"""
    return html_page
