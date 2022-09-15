# types-circuitpython

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/types-circuitpython?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/types-circuitpython?style=flat-square)

Type Support (typings) for [CircuitPython](https://github.com/adafruit/circuitpython) built-in binding packages.

Coding with `adafruit-circuitpython-typing`:

![adafruit-circuitpython-typing](https://raw.githubusercontent.com/hardfury-labs/types-circuitpython/master/screen-records/adafruit-circuitpython-typing.gif)

Coding with `types-circuitpython`:

![types-circuitpython](https://raw.githubusercontent.com/hardfury-labs/types-circuitpython/master/screen-records/types-circuitpython.gif)

## Long term support versions

Following [CircuitPython release versions](https://github.com/adafruit/circuitpython/releases)

[Pypi versions](https://pypi.org/project/types-circuitpython/#history)

- 7.x
  - 7.3.3
  - 7.3.2
  - 7.3.1
  - 7.3.0
- 8.x
  - 8.0.0b0 (8.0.0-beta.0)
  - 8.0.0a1 (8.0.0-alpha.1)
  - 8.0.0a0 (8.0.0-alpha.0)

## Usage

```bash
$ pip install types-circuitpython==7.3.3
# or
$ pip install types-circuitpython==8.0.0b0
```

## Development

## Initialization

```bash
$ virtualenv .venv
$ . ./.venv/bin/activate
$ pip install -r requirements.txt
$ python setup.py develop
# or
$ pip install -e .
```

## Generate bindings

```bash
$ make generate version=<CIRCUITPYTHON VERSION>
```

## Code styles

```bash
$ make format
$ make lint
```
