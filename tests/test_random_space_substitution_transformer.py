import pytest

from pirebok.transformers.random_space_substitution_transformer import RandomSpaceSubstitutionTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomSpaceSubstitutionTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = " <script> "

    result = transformer.transform(payload)

    assert result != payload
