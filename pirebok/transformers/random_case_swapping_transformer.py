import random

from pirebok.transformers.transformer import Transformer


class RandomCaseSwappingTransformer(Transformer):
    def transform(self, payload: str) -> str:
        return "".join(map(lambda x: x.swapcase() if random.random() > 0.5 else x, payload))
