import pytest

from pirebok.transformers.random_number_encoding_transformer import RandomNumberEncodingTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomNumberEncodingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "admin' OR 42=42#"

    result = transformer.transform(payload)

    assert result != payload
