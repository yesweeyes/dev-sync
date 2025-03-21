from google import genai
from config import GEMINI_API_KEY

GEMINI_1DOT5_FLASH_MODEL = "gemini-1.5-flash-8b"

client = genai.Client(api_key=GEMINI_API_KEY)

def gemini_generate_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(model=GEMINI_1DOT5_FLASH_MODEL, contents=[prompt])

        # Ensure response structure is correct
        if hasattr(response, "text"):
            return response.text
        
        return "No valid response received from Gemini API."
    
    except Exception as e:
        return f"Error: {str(e)}"

