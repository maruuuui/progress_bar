# Djangoでプログレスバー表示

## 前提

Windows 10
Python 3.7.4
django

## プロジェクト用ディレクトリ作成

以下のコマンドを実行して適当な場所にDjangoプロジェクトを格納するためのディレクトリを作成し、その中に入ります。

```bash
mkdir progress_bar  # ディレクトリ作って
cd progress_bar     # その中に入る
```

## 仮想環境の作成

既にインストールされているパッケージの影響を受けることを避けるため、新しく作った仮想環境内で1から環境構築していきます。
今回はパッケージ管理に`pipenv`を使用します。入っていない場合は、

```bash
pip install pipenv  # pipでインストール
```

を実行した後に、

```bash
export PIPENV_VENV_IN_PROJECT=true  # 仮想環境をプロジェクトディレクトリ配下に作るように設定
pipenv shell                        # 仮想環境作成！
```

これでまっさらな環境が作成できました。これ以降のコマンドは`pipenv shell`を実行して仮想環境に入った状態で実行することとします。

## djangoのインストール

以下のコマンドを実行してDjangoをインストールします。

```bash
pipenv install django
```

## プロジェクトの作成

以下のコマンドを実行してprojectを作成します。

```bash
django-admin startproject config .  #今のディレクトリにprojectを作成
```

現在のファイル構成は以下のようになります。

```bash
progress_bar
|--.venv
|--config
| |--__init__.py
| |--settings.py
| |--urls.py
| |--wsgi.py
|--djangodoc.md
|--manage.py
|--Pipfile
|--Pipfile.lock
```

## アプリの作成

`manage.py`と同階層で以下のコマンドを実行します。

```bash
mkdir apps                          #アプリ用ディレクトリ作成
cd apps                             #その中に…
python ../manage.py startapp example_app   #アプリ作成
```

作成したアプリを利用できるようにするために`config/settings.py`に以下の内容を追記します。

```python
# config/settings.py

INSTALLED_APPS = +["apps.example_app.apps.ExampleAppConfig"]
```

アプリをアプリ用ディレクトリ内に作ったため、このままでは今後の操作でエラーが出るため`apps.py`を編集して対応。

```python
# apps/example_app/apps.py
from django.apps import AppConfig


class ExampleAppConfig(AppConfig):
    # name = 'example_app'
    name = "apps.example_app"
```

## トップページのviewの作成

```python
# apps/example_app/views.py
```

## テンプレートの作成

## urlの設定

## 表示確認

## 時間のかかる処理を実行するボタンの設置

## プログレスバー作成手順

<https://getbootstrap.com/docs/4.3/components/progress/>を参考にプログレスバー部分を構築します。
