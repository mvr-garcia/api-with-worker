.PHONY: all format

all: format check

format:
	isort .
	black .

check:
	mypy .
	isort --check .
	black --check .
