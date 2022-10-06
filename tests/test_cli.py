from click.testing import CliRunner

from pirebok import cli


def test_cli():
    payload = "SELECT 42 /*forty-two*/"

    runner = CliRunner()
    result = runner.invoke(cli.main, ["-f", "RandomGenericFuzzer", "-p", payload])
    assert result.output != payload
