import pytest

from pirebok.transformers import RandomCaseSwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCaseSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "admin' OR 1=1#"

    result = transformer.transform(payload)

    assert result != payload
