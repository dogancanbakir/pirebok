import random

from pirebok.transformers.sql_transformer import SqlTransformer
from pirebok.transformers.utils import filter_candidates, replace_random


class RandomKeywordSwappingTransformer(SqlTransformer):
    def __init__(self) -> None:

        self.symbols = {
            # OR
            "||": [" OR ", " || "],
            " || ": [" OR ", "||"],
            "OR": [" OR ", "||"],
            "  OR  ": [" OR ", "||", " || "],
            # AND
            "&&": [" AND ", " && "],
            " && ": ["AND", " AND ", " && "],
            "AND": [" AND ", "&&", " && "],
            "  AND  ": [" AND ", "&&"],
            # Not equals
            "<>": ["!=", " NOT LIKE "],
            "!=": [" != ", "<>", " <> ", " NOT LIKE "],
            # Equals
            " = ": [" LIKE ", "="],
            "LIKE": [" LIKE ", "="],
        }

    def transform(self, payload: str) -> str:
        symbols_in_payload = filter_candidates(self.symbols, payload)

        if not symbols_in_payload:
            return payload

        candidate_symbol = random.choice(symbols_in_payload)
        replacements = self.symbols[candidate_symbol]
        candidate_replacement = random.choice(replacements)
        return replace_random(payload, candidate_symbol, candidate_replacement)
