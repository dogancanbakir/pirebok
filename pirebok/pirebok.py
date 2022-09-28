from pirebok.fuzzers import Fuzzer, RandomFuzzer
from pirebok.transformers import Transformer


def random_fuzzer() -> Fuzzer:
    transformers = [cls() for cls in Transformer.__subclasses__()]  # type: ignore
    return RandomFuzzer(transformers)
