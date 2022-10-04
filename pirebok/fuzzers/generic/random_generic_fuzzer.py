import random

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.generic_fuzzer import GenericFuzzer


class RandomGenericFuzzer(GenericFuzzer):
    def fuzz(self, payload: str) -> str:
        return random.choice(self.transformers).transform(payload)

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_generic(self)
