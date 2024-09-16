from pydantic import BaseModel


class GeminiConfig(BaseModel):
    api_key: str
    llm_model: str
