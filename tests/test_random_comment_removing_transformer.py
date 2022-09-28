import pytest

from pirebok.transformers import RandomCommentRemovingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCommentRemovingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "SELECT 1 /*forty-two*/"

    result = transformer.transform(payload)

    assert result != payload
