import pytest

from pirebok.transformers.space_transformer import SpaceTransformer


@pytest.fixture
def transformer():
    return SpaceTransformer()


def test_mutation(transformer):
    payload = " <script> "

    result = transformer.transform(payload)

    assert result != payload
