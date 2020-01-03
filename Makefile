.PHONY: all clean

all: build

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload --repository pypi dist/*

clean:
	rm -rf dist build