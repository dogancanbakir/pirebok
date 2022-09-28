import random
import re

from pirebok.transformers.transformer import Transformer

# TODO: maybe support diff comment styles? Add more replacements


class RandomCommentRemovingTransformer(Transformer):
    def transform(self, payload: str) -> str:
        positions = list(re.finditer(r"(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)|(--.*)", payload))

        if not positions:
            return payload

        pos = random.choice(positions).span()
        replacements = ["/**/"]
        replacement = random.choice(replacements)

        return payload[: pos[0]] + replacement + payload[pos[1] :]
