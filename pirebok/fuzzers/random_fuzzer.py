import random
from typing import Set

from pirebok.fuzzers import Fuzzer


class RandomFuzzer(Fuzzer):
    def fuzz(self, payload: str, epoch: int, batch_size: int) -> Set[str]:
        payloads = set()
        for _ in range(epoch):
            for _ in range(batch_size):
                payloads.add(random.choice(self.transformers).transform(payload))

        return payloads
