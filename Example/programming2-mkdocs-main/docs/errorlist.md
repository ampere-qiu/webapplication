# Pythonの基本的なエラー一覧

!!! abstract "目的"
    Pythonの基本的なエラーを知る。

## :material-chevron-right:構文のエラー

### SyntaxError

コロン`:`の付け忘れなど不正な構文のエラー。

``` py title="コロンの付け忘れ"
for i in range(5)  # コロンの付け忘れ
    print(i)

# SyntaxError: invalid syntax
```

### IndentationError

タブとソフトタブ（複数の半角スペース）のようにインデントが混合していたり、同一階層のインデントが揃っていなかったりしたときのエラー。

``` py title="タブの混合"
for i in range(5):
	print(i)  # タブ
    print(i)  # ソフトタブ（半角スペース4個）

# IndentationError: unindent does not match any outer indentation level
```

``` py title="インデントの不揃い"
for i in range(5):
    print(i)
  print(i)  # インデントが揃っていない

# IndentationError: unindent does not match any outer indentation level
```

## :material-chevron-right:値・タイプのエラー

### NameError

未定義の変数名を参照するなど名前が見つからないときのエラー。

``` py title="未定義変数の参照"
for i in range(5):
    print(x)  # 定義されていない変数xを参照している

# NameError: name 'x' is not defined
```

### TypeError

関数や演算子による処理のときに、不適切な型の値を利用したときのエラー。

``` py title="引数の個数の不一致"
def add(x, y):
    return x + y

add(1)  # 実引数が一つ足りない

# TypeError: add() missing 1 required positional argument: 'y'
```

``` py title="引数の個数の不一致"
l = []
l.append()  # 実引数が一つ必須

# TypeError: list.append() takes exactly one argument (0 given)d() missing 1 required positional argument: 'y'
```

``` py title="引数の型の不一致"
print(float(['130.5431', '35.123']))  # 文字列か整数以外の値を実引数として与えている

# TypeError: float() argument must be a string or a number, not 'list'
```

``` py title="異なる型の値の比較演算"
print(3 < 'a')  # 数字の3と文字列aを比較している

# TypeError: '<' not supported between instances of 'int' and 'str'
```

``` py title="異なる型の値の算術演算"
print(3 + 'a')  # 数字の3と文字列aを足している

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### AttributeError

存在しない属性を参照したときのエラー

``` py title="存在しない属性の参照"
class Stop:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

ritsumeikan = Stop(35.03497163, 135.72602961)
print(ritsumeikan.routes)  # Stopクラスに存在しない属性routesを参照している

# AttributeError: 'Stop' object has no attribute 'routes'
```

### IndexError

リストの長さを超えたインデックスを使って、範囲外の位置の要素を参照したときのエラー。

``` py title="リストの範囲外の参照"
l = [10, 20, 30]
print(l[3])  # リストの長さが3なので、インデックスの最大値は2なのに、3を指定している

# IndexError: list index out of range
```

### KeyError

辞書に登録されていないキーを使って値を参照したときのエラー。

``` py title="未登録のキーによる参照"
bearing = {'E': '東', 'W': '西', 'S': '南', 'N': '北'}
print(bearing['M'])  # 未登録のキー'M'を使って辞書の値を参照している

# KeyError: 'M'
```

## :material-chevron-right:ファイル・モジュールのエラー

### FileNotFoundError

読み込もうとしているファイルが見つからないときのエラー。ファイルへのパスが正しいか要確認。

``` py title="ファイルと異なるディレクトリで実行"
fi = open('kyotocitybus_stop.dat', 'r', encoding='utf-8')  # プログラムを実行しているディレクトリに存在しないデータファイルを読み込んでいる
line = fi.readline()
print(line)

# FileNotFoundError: [Errno 2] No such file or directory: 'kyotocitybus_stop.dat'
```

### ModuleNotFoundError

インポートしようとしているプログラムが見つからないときのエラー。プログラムへのパスが正しいか要確認。外部モジュールの場合は、`pip list`を実行してそのモジュールをインストール済みか要確認。

``` py title="インポートしたいプログラムと異なるディレクトリで実行"
import def_stop  # プログラムを実行しているディレクトリに存在しないプログラムをインポートしている


stop = def_stop.Stop(35.03497163, 135.72602961)

# ModuleNotFoundError: No module named 'def_stop'
```
