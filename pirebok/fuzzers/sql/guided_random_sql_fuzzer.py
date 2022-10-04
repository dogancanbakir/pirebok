import random

from metamaska.metamaska import Metamaska

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer


class GuidedRandomSqlFuzzer(SqlFuzzer):
    def fuzz(self, payload: str) -> str:
        metamask = Metamaska()
        payload_buff = random.choice(self.transformers).transform(payload)
        if metamask.form(payload_buff) == "valid":
            return payload_buff
        return payload

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_sql(self)
