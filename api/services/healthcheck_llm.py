from api.utils.gemini_client import gemini_generate_response


class HealthCheckLLMService:
    def __init__(self):
        pass

    def healthcheck_llm(self) -> str:
        healthcheck_response: str = gemini_generate_response(prompt="How does AI Work?")
        return healthcheck_response