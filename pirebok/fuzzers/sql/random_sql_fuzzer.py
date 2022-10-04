import random

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer


class RandomSqlFuzzer(SqlFuzzer):
    def fuzz(self, payload: str) -> str:
        return random.choice(self.transformers).transform(payload)

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_sql(self)
