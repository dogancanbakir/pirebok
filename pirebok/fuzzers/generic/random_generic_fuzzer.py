import random
from typing import Set

from pirebok.fuzzers import GenericFuzzer
from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor


class RandomGenericFuzzer(GenericFuzzer):
    def fuzz(self, payload: str, epoch: int, batch_size: int) -> Set[str]:
        payloads = set()
        for _ in range(epoch):
            for _ in range(batch_size):
                payloads.add(random.choice(self.transformers).transform(payload))

        return payloads

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_generic(self)
