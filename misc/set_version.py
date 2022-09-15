import re
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


@click.command()
@click.option("-v", "--version", "version", required=True, type=str, help="Version to set")
def main(version: str) -> None:
    content = read_file(SETUP_FILEPATH)

    overwrite_file(SETUP_FILEPATH, re.sub(VERSION_REGEX, '__version__ = "{}"'.format(version), content))


if __name__ == "__main__":
    main()
