# 開発用

```
# 必要なライブラリをインストール
$ pip install wheel twine setuptools

# ビルド
$ python setup.py bdist_wheel

$ twine upload --repository testpypi dist/*
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

```