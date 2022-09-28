from abc import ABC, abstractmethod


class Transformer(ABC):
    @abstractmethod
    def transform(self, payload: str) -> str:
        pass
