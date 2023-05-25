import re
import sys
from os.path import abspath, dirname, join

import click

HERE = abspath(dirname(__file__))
PROJECT = abspath(join(HERE, ".."))

SETUP_FILEPATH = join(PROJECT, "setup.py")

VERSION_REGEX = r'__version__ = "(.*)"'


def read_file(file_path: str) -> str:
    """Read file"""

    with open(file_path, "r") as f:
        return f.read()


def overwrite_file(file_path: str, content: str) -> None:
    """Overwrite file content."""

    with open(file_path, "w") as f:
        f.write(content)


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    pass


@cli.command("set", help="Set version in setup.py")
@click.option("-v", "--version", "version", required=True, type=str, help="Version to set")
def set_version(version: str) -> None:
    content = read_file(SETUP_FILEPATH)

    overwrite_file(SETUP_FILEPATH, re.sub(VERSION_REGEX, '__version__ = "{}"'.format(version), content))


@cli.command("check", help="Check version in setup.py")
def check_version() -> None:
    content = read_file(SETUP_FILEPATH)

    results = re.findall(VERSION_REGEX, content)

    if len(results) != 1 or results[0] != "0.0.0":
        print("Version is not reset, please reset it in setup.py")
        sys.exit(1)


@cli.command("reset", help="Reset version in setup.py")
def reset_version() -> None:
    content = read_file(SETUP_FILEPATH)

    overwrite_file(SETUP_FILEPATH, re.sub(VERSION_REGEX, '__version__ = "0.0.0"', content))


if __name__ == "__main__":
    cli()
