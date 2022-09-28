import click


@click.command(no_args_is_help=True)
@click.option('-p', '--payload', help="payload to fuzz")
def main(payload):
    if not payload:
        raise ValueError("payload is required.")

    click.echo("")


if __name__ == "__main__":
    main()  # pragma: no cover
