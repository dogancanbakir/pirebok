import pytest

from pirebok.transformers import RandomKeywordSwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomKeywordSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "admin' OR 1=1#"

    result = transformer.transform(payload)

    assert result != payload
