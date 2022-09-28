import random

from pirebok.transformers.transformer import Transformer
from pirebok.transformers.utils import random_string, replace_random


class RandomCommentRewritingTransformer(Transformer):
    def transform(self, payload: str) -> str:

        rnd = random.random()

        if rnd < 0.5 and ("#" in payload or "-- " in payload):
            return payload + random_string(2)

        if rnd >= 0.5 and ("*/" in payload):
            return replace_random(payload, "*/", random_string() + "*/")

        return payload
