from abc import ABC, abstractmethod

from pirebok.fuzzers.generic_fuzzer import GenericFuzzer
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer


class FuzzerVisitor(ABC):
    @abstractmethod
    def visit_generic(self, fuzzer: GenericFuzzer) -> None:
        pass

    @abstractmethod
    def visit_sql(self, fuzzer: SqlFuzzer) -> None:
        pass
