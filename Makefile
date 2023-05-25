generate:
	git submodule update --remote
# git submodule update --init
	cd circuitpython/ && git checkout $(version) && cd ..
	git submodule
	rm -rf bindings/
	python circuitpython/tools/extract_pyi.py circuitpython/shared-bindings bindings
# reformatted & lint
	make format

format:
	black bindings

lint:
	pyright bindings

pre-commit:
	pre-commit install
	pre-commit run --all-files

build-package:
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
	rm -rf dist/
	python -m build

publish:
	twine upload dist/*

showhand:
	make generate
	python misc/version.py set --version $(version)
	make build-package
	make publish
	python misc/version.py reset
