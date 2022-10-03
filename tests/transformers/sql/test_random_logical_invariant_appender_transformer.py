import pytest

from pirebok.transformers import RandomLogicalInvariantAppenderTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomLogicalInvariantAppenderTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "admin' OR 1=1#"

    result = transformer.transform(payload)

    assert result != payload
