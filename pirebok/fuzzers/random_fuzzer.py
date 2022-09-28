import random
from typing import List

from pirebok.fuzzers import Fuzzer
from pirebok.transformers import Transformer


class RandomFuzzer(Fuzzer):
    def __init__(self, transformers: List[Transformer]) -> None:
        self.transformers = transformers

    def fuzz(self, payload: str) -> str:
        transformer = random.choice(self.transformers)
        payload = transformer.transform(payload)
        return payload
