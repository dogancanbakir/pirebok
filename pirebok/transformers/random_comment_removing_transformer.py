import random
import re

from pirebok.transformers.generic_transformer import GenericTransformer

# TODO: maybe support diff comment styles? E.g., //, #, --, <!-- -->, ;, ', *, !
# If we add all the comment styles, this might cause an err in certain cases, like url anchor links
#  Add more replacements


class RandomCommentRemovingTransformer(GenericTransformer):
    def transform(self, payload: str) -> str:
        positions = list(re.finditer(r"(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)", payload))

        if not positions:
            return payload

        pos = random.choice(positions).span()
        replacements = ["/**/"]
        replacement = random.choice(replacements)

        return payload[: pos[0]] + replacement + payload[pos[1] :]
