import pytest

from pirebok.fuzzers import FuzzerBuilder, RandomGenericFuzzer


@pytest.fixture
def builder() -> FuzzerBuilder:
    return FuzzerBuilder()


def test_creation(builder: FuzzerBuilder) -> None:
    fuzzer_name = "RandomGenericFuzzer"

    fuzzer = builder.choice(fuzzer_name).threshold(0.5).build()

    assert isinstance(fuzzer, RandomGenericFuzzer)
