from typing import Any, List, Type

from pirebok.fuzzers import Fuzzer
from pirebok.transformers import Transformer


def fuzzers() -> List[Type[Fuzzer]]:
    return Fuzzer.__subclasses__()


def get_fuzzer(name: str) -> Any:
    transformers = [cls() for cls in Transformer.__subclasses__()]  # type: ignore

    for fuzzer in fuzzers():
        if name == fuzzer.__name__:
            return fuzzer(transformers)

    return None
