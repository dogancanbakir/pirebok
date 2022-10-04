import click
from tqdm.auto import trange

from pirebok.fuzzers import Fuzzer, FuzzerBuilder


@click.command(no_args_is_help=True)
@click.option(
    '-f',
    '--fuzzer',
    required=True,
    type=click.Choice(
        [ff.__name__ for f in Fuzzer.__subclasses__() for ff in f.__subclasses__()], case_sensitive=False
    ),
    help="choose fuzzer",
)
@click.option('-s', '--steps', default=10, help="Number of iteration")
@click.option('-p', '--payload', required=True, help="payload to fuzz")
def main(fuzzer: str, steps: int, payload: str) -> None:
    fuzzer_builder = FuzzerBuilder()
    fzzer = fuzzer_builder.choice(fuzzer).build()
    print('\n'.join(map(str, set(map(lambda _: fzzer.fuzz(payload), trange(steps))))))


if __name__ == "__main__":
    main()  # pragma: no cover
