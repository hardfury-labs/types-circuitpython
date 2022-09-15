from os import listdir, path

from setuptools import setup

__name__ = "types-circuitpython"
__version__ = "0.0.0"
__repo__ = "https://github.com/hardfury-labs/types-circuitpython"
__author__ = "HardFury"


HERE = path.abspath(path.dirname(__file__))
BINDINGS_DIR = path.join(HERE, "bindings")

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def list_dir(_dir, sort=True):
    """List directory"""

    dirs = listdir(_dir)

    if sort:
        dirs.sort()

    return dirs


PACKAGES = []
PACKAGE_DIR = {}
PACKAGE_DATA = {}

for package in list_dir(BINDINGS_DIR):
    if package.endswith(".egg-info"):
        continue

    if path.isfile(path.join(BINDINGS_DIR, package)):
        continue

    PACKAGES.append(package)
    PACKAGE_DIR[package] = "bindings/{}".format(package)
    PACKAGE_DATA[package] = ["*.pyi", "py.typed"]

# https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
setup(
    name=__name__,
    version=__version__,
    url=__repo__,
    author=__author__,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Hardware",
        "Typing :: Typed",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="GNU General Public License v3 (GPLv3)",
    description="Type support (typings) for CircuitPython built-in binding packages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["circuitpython", "micropython", "adafruit"],
    python_requires=">=3.7.0",
    install_requires=["adafruit-circuitpython-typing"],
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    package_data=PACKAGE_DATA,
)
