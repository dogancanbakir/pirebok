import pytest

from pirebok.transformers.random_case_transformer import RandomCaseTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCaseTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = " <script> "

    result = transformer.transform(payload)

    assert result != payload
