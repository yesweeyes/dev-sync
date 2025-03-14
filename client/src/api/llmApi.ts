import api from "./config"
import { HEALTHCHECK_LLM } from "./routes/llm"

const llmApi = {
    healthcheck: () => api.get(HEALTHCHECK_LLM),
}

export default llmApi;