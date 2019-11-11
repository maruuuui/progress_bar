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
from django.shortcuts import render


def index(request):
    """基本となるページ"""
    return render(request, "example_app/index.html")
```

## テンプレートの作成

```html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="utf-8" />
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!-- jQuery,Popper.js,Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>

    <title>プログレスバーサンプル</title>
</head>

<body>
    <div class="container">
        <div class="card">
            <div class="card-header">
                プログレスバーサンプル
            </div>
            <div class="card-body">
                <div id="progress">プログレスバー表示部分</div>
                <div id="result">処理結果表示部分</div>
                <div class="row">
                    <button class="btn btn-primary col-12" id="start_button">処理の実行</button>
                </div>
            </div>
        </div>
    </div>
</body>
<script>
    //プログレスバー表示部分の初期状態
    const progresshtml = '<div id="progress">プログレスバー表示部分</div>';
    
const setup_url = "{% url 'setup' %}"
    $("#start_button").on("click", function (event) {
        //setIntervalのタイマーID。clearInterval(timer_id)でタイマーを止めるのに使用する
        let timer_id;
        
        console.log("start")
        $("#start_button").attr({ "disabled": true })
        $.get(url, {},
            function (data) {
                console.log("get")
                let pk = data
                console.log("Data Loaded: " + data);
                //2000msごとにプログレスバーを更新し始める
                timer_id = setInterval(function () { ShowProgressBar(pk) }, 2000)
                //時間のかかる処理を開始する
                GetResult(pk)
            }
        );


        function ShowProgressBar(progress_pk) {
            $.get("{% url 'show_progress' %}", { progress_pk: progress_pk },
                function (data) {
                    console.log("Data Loaded: " + data);
                    //プログレスバーを表示
                    $("#progress").replaceWith(data)
                }
            );
        }

        function GetResult(progress_pk) {
            $.get("{% url 'do_something' %}", { progress_pk: progress_pk },
                function (data) {
                    console.log("Data Loaded: " + data);
                    //プログレスバー取得をやめる
                    clearInterval(timer_id);
                    //プログレスバー部分を元の状態に戻す
                    $("#progress").replaceWith(progresshtml)
                    //処理結果表示
                    $("#result").replaceWith(data)
                    $("#start_button").attr({ "disabled": false })
                }
            );
        }
    });
</script>

</html>
```

## urlの設定

## 表示確認

## 時間のかかる処理を実行するボタンの設置

## プログレスバー部分

<https://getbootstrap.com/docs/4.3/components/progress/>を参考にプログレスバー部分を構築します。
