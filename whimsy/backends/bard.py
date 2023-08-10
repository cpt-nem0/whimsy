"""Bard client."""

from bardapi import Bard

from .. import config
from .base import BackendBase


class BardClient(BackendBase):
    def __init__(self) -> None:
        self._client = Bard(token=config.BARD_TOKEN)

    def ask(self, question: str) -> str:
        return self._client.get_answer(question)

    def get_answer(self, question: str) -> str:
        return self.ask(question)["content"]
