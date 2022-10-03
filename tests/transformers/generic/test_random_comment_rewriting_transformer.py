import pytest

from pirebok.transformers import RandomCommentRewritingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCommentRewritingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "# <script> /**/ "

    result = transformer.transform(payload)

    assert result != payload
