import click

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
@click.option('-e', '--epoch', default=1, help="Number of iteration")
@click.option('-b', '--batch_size', default=10, help="Total number of payload generation per epoch")
@click.option('-p', '--payload', required=True, help="payload to fuzz")
def main(fuzzer: str, epoch: int, batch_size: int, payload: str) -> None:
    fuzzer_builder = FuzzerBuilder()
    fzzer = fuzzer_builder.choice(fuzzer).build()
    print('\n'.join(map(str, fzzer.fuzz(payload, epoch, batch_size))))


if __name__ == "__main__":
    main()  # pragma: no cover
