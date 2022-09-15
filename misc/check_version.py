import re
import sys

from set_version import SETUP_FILEPATH, VERSION_REGEX, read_file


def main() -> None:
    content = read_file(SETUP_FILEPATH)

    results = re.findall(VERSION_REGEX, content)

    if len(results) != 1 or results[0] != "0.0.0":
        print("Version is not reset, please reset it in setup.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
