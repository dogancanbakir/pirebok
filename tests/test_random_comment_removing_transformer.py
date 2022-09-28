import pytest

from pirebok.transformers.random_comment_removing_transformer import RandomCommentRemovingTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCommentRemovingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "SELECT 1 /*forty-two*/"

    result = transformer.transform(payload)

    assert result != payload
