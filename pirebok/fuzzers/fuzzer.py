from abc import ABC, abstractmethod
from typing import Sequence, Set

from pirebok.transformers import Transformer


class Fuzzer(ABC):
    def __init__(self, transformers: Sequence[Transformer]) -> None:
        self.transformers = transformers

    @abstractmethod
    def fuzz(self, payload: str, epoch: int, batch_size: int) -> Set[str]:
        pass
