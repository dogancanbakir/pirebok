import pytest

from pirebok.transformers import RandomTautologySwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomTautologySwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "admin' OR 1=1#"

    result = transformer.transform(payload)

    assert result != payload
