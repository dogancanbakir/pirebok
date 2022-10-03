import random
from typing import Set

from tqdm.auto import trange

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.generic_fuzzer import GenericFuzzer


class RandomGenericFuzzer(GenericFuzzer):
    def fuzz(self, payload: str, epoch: int, batch_size: int) -> Set[str]:
        payloads = set()
        payload_buff = payload
        for _ in trange(epoch, desc="Epoch"):
            for _ in trange(batch_size, desc="Batch", leave=False):
                payload_buff = random.choice(self.transformers).transform(payload)
                payloads.add(payload_buff)

        return payloads

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_generic(self)
