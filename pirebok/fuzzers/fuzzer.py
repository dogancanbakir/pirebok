from abc import ABC, abstractmethod
from typing import Sequence

from pirebok.transformers import Transformer


class Fuzzer(ABC):
    def __init__(self, transformers: Sequence[Transformer]) -> None:
        self.transformers = transformers

    @abstractmethod
    def fuzz(self, payload: str) -> str:
        pass

    @abstractmethod
    def accept(self, visitor) -> None:
        visitor.visit_generic(self)
