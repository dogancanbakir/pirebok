import random

from pirebok.fuzzers.fuzzer import Fuzzer
from pirebok.transformers.transformer import Transformer


class RandomFuzzer(Fuzzer):
    def __init__(self, transformers: list[Transformer]) -> None:
        self.transformers = transformers

    def fuzz(self, payload: str) -> str:
        transformer = random.choice(self.transformers)
        payload = transformer.transform(payload)
        return payload
