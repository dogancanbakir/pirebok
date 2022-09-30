import random
import re

from pirebok.transformers.generic_transformer import GenericTransformer

# TODO: how about random char encoding?


class RandomNumberEncodingTransformer(GenericTransformer):
    def transform(self, payload: str) -> str:
        candidates = list(re.finditer(r'(?<=[^\'"\d\wx])\d+(?=[^\'"\d\wx])', payload))

        if not candidates:
            return payload

        candidate_pos = random.choice(candidates).span()
        candidate = payload[candidate_pos[0] : candidate_pos[1]]

        replacements = [hex(int(candidate))]
        replacement = random.choice(replacements)
        return payload[: candidate_pos[0]] + replacement + payload[candidate_pos[1] :]
