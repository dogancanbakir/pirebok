from __future__ import annotations

from typing import Optional, Sequence, Type

from pirebok.fuzzers import Fuzzer
from pirebok.transformers import GenericTransformer


class FuzzerBuilder:
    def __init__(self) -> None:
        self.fuzzer: Optional[Fuzzer] = None

    def _fuzzers(self) -> Sequence[Type[Fuzzer]]:
        return Fuzzer.__subclasses__()

    def _get_fuzzer(self, name: str) -> Optional[Fuzzer]:
        transformers = list(map(lambda x: x(), GenericTransformer.__subclasses__()))  # type: ignore

        return next(
            (fuzzer(transformers) for fuzzer in self._fuzzers() if (name and name.lower()) == fuzzer.__name__.lower()),
            None,
        )

    def choice(self, name: str) -> FuzzerBuilder:
        self.fuzzer = self._get_fuzzer(name)
        return self

    def build(self) -> Optional[Fuzzer]:
        return self.fuzzer
