# python-svg-generater

pythonを使って、cui操作でsvg画像を生成します。

svgの基礎的な知識がある人が使うことを前提にして作成しました。


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

| 命令      |  意味 |     インデックス      |
|:------------:|:------------:|:------------:|
|file name;|ファイル名の指定| - |
|1:vertical 2:oblong 3:square;|画像の縦横比| - |
|background;|背景色|cn|
|add new? y/n;|さらに要素を追加するか| - |
|1:rect 2:circle 3:text 4:path;|svg要素||
|ex(x= ;)|属性の指定||




### 2.エディタ操作で生成
```
$ python main2.py
```
