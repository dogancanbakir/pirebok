import pytest

from pirebok.transformers.space_transformer import SpaceTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return SpaceTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = " <script> "

    result = transformer.transform(payload)

    assert result != payload
