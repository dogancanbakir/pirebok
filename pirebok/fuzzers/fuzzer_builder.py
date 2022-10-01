from __future__ import annotations

from typing import List, Type

from pirebok.fuzzers import Fuzzer
from pirebok.fuzzers.fuzzer_transformer_resolver_visitor import FuzzerTransformerResolverVisitor


class FuzzerBuilder:
    def __init__(self) -> None:
        self.fuzzer: Fuzzer

    def _fuzzers(self) -> List[Type[Fuzzer]]:
        return [ff for f in Fuzzer.__subclasses__() for ff in f.__subclasses__()]  # type: ignore

    def _get_fuzzer(self, name: str) -> Fuzzer:
        fuzzer = next(fuzzer([]) for fuzzer in self._fuzzers() if (name and name.lower()) == fuzzer.__name__.lower())
        visitor = FuzzerTransformerResolverVisitor()
        fuzzer.accept(visitor)
        fuzzer.transformers = visitor.transformers

        return fuzzer

    def choice(self, name: str) -> FuzzerBuilder:
        self.fuzzer = self._get_fuzzer(name)
        return self

    def build(self) -> Fuzzer:
        return self.fuzzer
