import random

from pirebok.transformers.generic_transformer import GenericTransformer
from pirebok.transformers.utils import random_string, replace_random

# TODO: maybe support diff comment styles? E.g., //, #, --, <!-- -->, ;, ', *, !
# If we add all the comment styles, this might cause an err in certain cases, like url anchor links
#  Add more replacements


class RandomCommentRewritingTransformer(GenericTransformer):
    def transform(self, payload: str) -> str:

        rnd = random.random()

        if rnd < 0.5 and ("#" in payload or "-- " in payload):
            return payload + random_string(2)

        if rnd >= 0.5 and ("*/" in payload):
            return replace_random(payload, "*/", random_string() + "*/")

        return payload
