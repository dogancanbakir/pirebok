import random
from typing import Sequence

from metamaska.metamaska import Metamaska

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer
from pirebok.transformers import Transformer


class GuidedRandomSqlFuzzer(SqlFuzzer):
    def __init__(self, transformers: Sequence[Transformer]) -> None:
        super().__init__(transformers)
        self.threshold: float

    def fuzz(self, payload: str) -> str:
        # TODO:move this out
        metamask = Metamaska()
        payload_buff = random.choice(self.transformers).transform(payload)
        cls, proba = metamask.form(payload_buff, True)
        if cls == "sqli" and proba < self.threshold:
            return payload_buff
        return payload

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_sql(self)
