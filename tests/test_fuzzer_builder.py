import pytest

from pirebok.fuzzers import FuzzerBuilder, RandomFuzzer


@pytest.fixture
def builder() -> FuzzerBuilder:
    return FuzzerBuilder()


def test_creation(builder: FuzzerBuilder) -> None:
    fuzzer_name = "RandomFuzzer"

    fuzzer = builder.choice(fuzzer_name).build()

    assert isinstance(fuzzer, RandomFuzzer)
