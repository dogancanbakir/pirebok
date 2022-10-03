import random
import re

from pirebok.transformers.sql_transformer import SqlTransformer
from pirebok.transformers.utils import number_tautology, string_tautology


class RandomTautologySwappingTransformer(SqlTransformer):
    def transform(self, payload: str) -> str:
        results = list(re.finditer(r'((?<=[^\'"\d\wx])\d+(?=[^\'"\d\wx]))=\1', payload))
        if not results:
            return payload

        candidate = random.choice(results)

        replacements = [string_tautology(), number_tautology()]
        replacement = random.choice(replacements)
        new_payload = payload[: candidate.span()[0]] + replacement + payload[candidate.span()[1] :]
        return new_payload
