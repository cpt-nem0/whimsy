import google.generativeai as genai

from .base import BackendBase


class GeminiClient(BackendBase):
    def __init__(self, api_key: str, model_name: str):
        super().__init__(None, api_key, model_name)

    @staticmethod
    def available_models() -> list[str]:
        models = ["gemini-1.5-flash"]
        return models

    def initialize(self):
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)

    @BackendBase._ensure_model_initialized_decorator
    def _query_prompt(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text

    @BackendBase._ensure_model_initialized_decorator
    def get_token_limits(self) -> tuple[int, int]:
        return self.model.input_token_limit, self.model.output_token_limit

    @BackendBase._ensure_model_initialized_decorator
    def get_token_count(self, prompt: str):
        return self.model.count_token(prompt)
