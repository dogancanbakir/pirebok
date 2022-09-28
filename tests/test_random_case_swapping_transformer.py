import pytest

from pirebok.transformers.random_case_swapping_transformer import RandomCaseSwappingTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCaseSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = " <script> "

    result = transformer.transform(payload)

    assert result != payload
