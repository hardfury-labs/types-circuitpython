import os

import requests
from loguru import logger

# from setuptools.extern.packaging import version
from setuptools._vendor.packaging import version


def get_circuitpython_versions() -> list:
    url = "https://api.github.com/repos/adafruit/circuitpython/releases"
    response = requests.get(url, headers={"Accept": "application/vnd.github+json"}, params={"per_page": 100})

    releases = response.json()

    versions = []

    for release in releases:
        tag_name = release.get("tag_name")
        versions.append(tag_name)

    return versions


def get_published_versions() -> list:
    url = "https://pypi.org/simple/types-circuitpython/"
    response = requests.get(url, headers={"Accept": "application/vnd.pypi.simple.v1+json"})

    info = response.json()

    return info.get("versions", [])


def main():
    published_versions = get_published_versions()
    logger.info("Published versions: {}".format(", ".join(published_versions)))

    for circuitpython_version in get_circuitpython_versions():
        formatted_version = version.Version(circuitpython_version)

        if formatted_version.major in [7, 8] and str(formatted_version) not in published_versions:
            logger.info("Preparing CircuitPython=={}".format(circuitpython_version))
            os.system("make showhand version={}".format(circuitpython_version))


if __name__ == "__main__":
    main()
