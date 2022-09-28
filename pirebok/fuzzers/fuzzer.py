from abc import ABC, abstractmethod


class Fuzzer(ABC):
    @abstractmethod
    def fuzz(self, payload: str) -> str:
        pass
