.PHONY: all clean test

all: build

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload --repository pypi dist/*

test: 
	python setup.py test
	
clean:
	rm -rf dist build