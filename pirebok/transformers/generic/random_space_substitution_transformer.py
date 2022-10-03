import random
import uuid

from pirebok.transformers.generic_transformer import GenericTransformer
from pirebok.transformers.utils import filter_candidates, replace_random

# TODO: make this more generic


class RandomSpaceSubstitutionTransformer(GenericTransformer):
    def __init__(self) -> None:
        self.symbols = {
            " ": [
                "/**/",
                "/**//**/",
                "/**//**//**/",
                f"%%23{uuid.uuid4().hex[1:5]}%%0A",
                "--",
                "+",
                "%09",
                "%0A",
                "%0C",
                "%0D",
                "%00",
                "\t",
                "\n",
                "\f",
                "\v",
                "\xa0",
            ],
            "\t": [" ", "\n", "\f", "\v", "\xa0"],
            "\n": ["\t", " ", "\f", "\v", "\xa0"],
            "\f": ["\t", "\n", " ", "\v", "\xa0"],
            "\v": ["\t", "\n", "\f", " ", "\xa0"],
            "\xa0": ["\t", "\n", "\f", "\v", " "],
        }

    def transform(self, payload: str) -> str:

        symbols_in_payload = filter_candidates(self.symbols, payload)

        if not symbols_in_payload:
            return payload

        candidate_symbol = random.choice(symbols_in_payload)
        replacements = self.symbols[candidate_symbol]
        candidate_replacement = random.choice(replacements)
        return replace_random(payload, candidate_symbol, candidate_replacement)
