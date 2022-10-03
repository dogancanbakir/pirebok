import random

from pirebok.transformers.generic_transformer import GenericTransformer


class RandomCaseSwappingTransformer(GenericTransformer):
    def transform(self, payload: str) -> str:
        return "".join(map(lambda x: x.swapcase() if random.random() > 0.5 else x, payload))
