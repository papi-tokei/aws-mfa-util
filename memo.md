# 開発用

```
# 必要なライブラリをインストール
$ pip install wheel twine setuptools

# ビルド
$ make

# 前のビルド結果ファイルを削除
$ make clean

# pypiを更新
$ make upload

# テスト
$ make test
```

# デバッグ用

```
# setup.pyがあるディレクトリで
$ pip install .
```