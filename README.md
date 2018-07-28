# python-svg-generater

pythonを使って、cui操作でsvg画像を生成します。

svgの基礎的な知識がある方が使うことを前提にして作成しました。

主にsvgタグは選択式、その属性は簡単な文字列で指定
して出力できるようにしています。


## ファイル構成
    .
    ├── README.md
    ├── main.py
    ├── main2.py
    ├── funcs.py
    └── write.py

## 環境構築

python3をインストール
> https://www.python.org/downloads/


プログラムのインストール
```
$ git clone https://github.com/nari19/python-svg-generator.git
$ cd python-svg-generater
```

-----------

## 機能

### 1.ターミナルでの対話入力で生成
```
$ python main.py
```

実行すると以下が順番に聞かれます。

|              | 命令          |     意味     |
|:------------:|:------------:|:------------:|
|1|file name;|作成するファイル名の指定|
|2|1:vertical 2:oblong 3:square;|画像の縦横比|
|3|background;|背景色|
|4|add new? y/n; |さらに要素を追加するか|
||||
||-|y(Yes)を指定|
|5|1:rect 2:circle 3:text 4:path;|svg要素|
|6|ex(x= ;)|属性の指定|
|7|add new? y/n; |さらに要素を追加するか|
||||
||-|n(No)を指定|
||-|終了|

4種類の要素いずれかを指定したのち属性を指定する、
という動作を"add new?"で"n"を入力するまで
繰り返します




### 2.エディタ操作で生成
```
$ python main2.py
```
