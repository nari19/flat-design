# python-svg-generater

pythonを使って、cui操作でsvg画像を生成します。

svgの基礎的な知識がある方が使うことを前提にして作成しました。

主にsvgタグは選択することで、その属性は簡単な文字列を指定することで
出力できるようにしています。

カレントディレクトリから一つ上の階層に画像が生成されます。


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
||-|y(Yes)を入力|
|5|1:rect 2:circle 3:text 4:path;|svg要素|
|6|ex(x= ;)|属性の指定|
|7|add new? y/n; |さらに要素を追加するか|
||||
||-|n(No)を入力|
||-|終了|

上記では、1,2,3の基本設定を行った後、add new?が聞かれ、y(Yes)を入力すると
4種類の要素いずれかを指定することができます。

"add new?"で"n"を入力するまで5,6,7の
要素の追加、またその属性の入力を
繰り返します。


またそれぞれの属性では、インデックスカラーのように
事前に定義した値を指定することができます。(funcs.py に記述)

<img src="/images/8.35.46.png" alt="funcs.py" width="400">


|              | 1            |     2        |     3        |     4        |
|:------------:|:------------:|:------------:|:------------:|:------------:|
|  インデックス  |rect|circle|text|path|
| - |||text ;|d=|
|wn|x= ;|cx= ;|x= ;||
|hn|y= ;|cy= ;|y= ;||
|wn|width= ;|r= ;|||
|hn|height= ;||||
|fn|||font-family= ;||
|wn, hn|||font-size= ;|
|cn|fill= ;|fill= ;|fill= ;|fill= ;|

wn,hnはそれぞれ、縦、横を10等分した値を指定することができます。

ex) w2 → 横幅2/10の値


### 2.エディタ操作で生成
```
$ python main2.py
```

コメントアウトを外して、関数を呼び出すと、次のようなsvg画像が作成されます。


<img src="/images/ 6.44.15.png" alt="main2.py" width="400">

|temp_color|temp_font|cross_square|
|---|---|---|
|<img src="/images/temp_color.svg" alt="temp_color" width="250">|<img src="/images/temp_font.svg" alt="temp_font" width="250">|<img src="/images/cross_square.svg" alt="cross_square" width="250">|

↑main.pyで呼び出せる色やフォントを確認できます。(funcs.pyで編集すれば内容が更新されます。)

このプログラムでSVGを作成するには以下のように書きます。
(具体的な説明は省略します)

例）斜めに正方形を並べる

``` py
# main2.py
def cross_square():
    t = ['cross_square2', '3', '#fff']
    x = 1
    for i in range(10):
        t += ['y', '1', 'w'+str(i), 'h'+str(i), 'w1', 'h1', 'c'+str(x)]
        x += 1
    t += ['n']
    t_edit(t)
```