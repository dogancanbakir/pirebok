import random
import re

from pirebok.transformers.sql_transformer import SqlTransformer
from pirebok.transformers.utils import number_contradiction, number_tautology, string_contradiction, string_tautology


class RandomLogicalInvariantAppenderTransformer(SqlTransformer):
    def transform(self, payload: str) -> str:
        match = re.search("(#|-- )", payload)

        if not match:
            return payload

        pos = match.start()

        replacement = random.choice(
            [
                # AND True
                " AND 1",
                " AND True",
                " AND " + number_tautology(),
                " AND " + string_tautology(),
                # OR False
                " OR 0",
                " OR False",
                " OR " + number_contradiction(),
                " OR " + string_contradiction(),
            ]
        )

        new_payload = payload[:pos] + replacement + payload[pos:]

        return new_payload
