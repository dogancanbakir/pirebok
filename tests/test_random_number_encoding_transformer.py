import pytest

from pirebok.transformers import RandomNumberEncodingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomNumberEncodingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "admin' OR 42=42#"

    result = transformer.transform(payload)

    assert result != payload
