import click

from pirebok.pirebok import random_fuzzer


@click.command(no_args_is_help=True)
@click.option('-r', '--random', default=True, help="choose random fuzzer (default)")
@click.option('-p', '--payload', help="payload to fuzz")
def main(payload: str, random: bool) -> None:
    if not payload:
        raise ValueError("payload is required.")

    if random:
        fuzzer = random_fuzzer()
        click.echo(fuzzer.fuzz(payload))


if __name__ == "__main__":
    main()  # pragma: no cover
