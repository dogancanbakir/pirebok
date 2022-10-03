import pytest

from pirebok.transformers import RandomSpaceSubstitutionTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomSpaceSubstitutionTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = " <script> "

    result = transformer.transform(payload)

    assert result != payload
