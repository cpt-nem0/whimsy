from abc import ABC, abstractmethod
from functools import wraps

from ..exceptions import ModelNotInitializedException


class BackendBase(ABC):

    def __init__(self, api_endpoint: str, api_key: str, model_name: str):
        if not api_key:
            raise ValueError("API key cannot be None or empty")

        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.model_name = model_name
        self.model = None

    def _ensure_model_initialized_decorator(func):
        """Decorator to check if the model has been initialized."""

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.model:
                raise ModelNotInitializedException("Please call 'initialize()' method.")
            return func(self, *args, **kwargs)

        return wrapper

    @staticmethod
    @abstractmethod
    def available_models(self) -> list[str]: ...

    @abstractmethod
    def _query_prompt(self, prompt: str): ...

    @abstractmethod
    def initialize(self): ...

    @abstractmethod
    def get_token_limits(self) -> tuple[int, int]: ...

    @abstractmethod
    def get_token_count(self, prompt: str): ...

    def get_answer(self, prompt: str):
        return self._query_prompt(prompt)
