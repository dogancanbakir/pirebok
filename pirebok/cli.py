from functools import reduce
from operator import iconcat

import click
from tqdm.auto import trange

from pirebok.fuzzers import Fuzzer, FuzzerBuilder


@click.command(no_args_is_help=True, context_settings={'show_default': True})
@click.option(
    "-f",
    "--fuzzer",
    required=True,
    type=click.Choice(
        map(lambda x: x.__name__, reduce(iconcat, map(lambda x: x.__subclasses__(), Fuzzer.__subclasses__()))),
        case_sensitive=False,
    ),
    help="choose fuzzer",
)
@click.option("-s", "--steps", default=10, help="Number of iteration")
@click.option("-t", "--threshold", default=0.5, help="Threshold for the guided fuzzers")
@click.option("-p", "--payload", required=True, help="Payload to fuzz")
def main(fuzzer: str, steps: int, threshold: float, payload: str) -> None:
    fuzzer_builder = FuzzerBuilder()
    fzzer = fuzzer_builder.choice(fuzzer).threshold(threshold).build()
    print("\n".join(map(repr, set(map(lambda _: fzzer.fuzz(payload), trange(steps))))))


if __name__ == "__main__":
    main()  # pragma: no cover
