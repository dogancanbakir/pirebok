import click

from pirebok.pirebok import fuzzers, get_fuzzer


@click.command(no_args_is_help=True)
@click.option('-l', '--list-fuzzers', is_flag=True, flag_value=True, help="list fuzzers")
@click.option('-f', '--fuzzer', help="choose fuzzer")
@click.option('-e', '--epoch', default=1, help="Number of iteration")
@click.option('-b', '--batch_size', default=10, help="Total number of payload generation per epoch")
@click.option('-p', '--payload', help="payload to fuzz")
def main(list_fuzzers: bool, fuzzer: str, epoch: int, batch_size: int, payload: str) -> None:

    if list_fuzzers:
        print('\n'.join(map(str, [f.__name__ for f in fuzzers()])))
        return

    if not payload:
        raise ValueError("payload is required.")

    if fuzzer:
        fzzer = get_fuzzer(fuzzer)
        if fzzer is None:
            print("Select one of the listed fuzzer")
            return
        print('\n'.join(map(str, fzzer.fuzz(payload, epoch, batch_size))))


if __name__ == "__main__":
    main()  # pragma: no cover
