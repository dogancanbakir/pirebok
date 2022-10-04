import random
from typing import Set

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer


class RandomSqlFuzzer(SqlFuzzer):
    def fuzz(self, payload: str, epoch: int, batch_size: int) -> Set[str]:
        payloads = set()
        payload_buff = payload
        for _ in range(epoch):
            for _ in range(batch_size):
                payload_buff = random.choice(self.transformers).transform(payload_buff)
                payloads.add(payload_buff)

        return payloads

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_sql(self)
