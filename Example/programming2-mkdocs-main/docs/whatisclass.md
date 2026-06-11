# クラスとは

!!! abstract "目的"
    クラスの意義を知る。

!!! check "キーワード"
    - クラス、属性
    - インスタンス、インスタンス変数
    - メソッド
    - 継承、サブクラス
    - ポリモーフィズム

## 複数の異なるデータを扱う

対応づけられる複数の情報を処理するプログラムを考えよう。

- 例：学生の*名前*と*履修科目の成績*
- 学生の名前リストと履修科目のリストを作り、同一学生の名前と履修科目を同じ順番（インデックス）で対応づけて管理すると…

``` py title="リスト間の対応付け"
names = ['太郎', '次郎']
classes_list = [{'アルゴリズム':5, 'データベース':3}, {'アルゴリズム':4, '人工知能':4}]
```

==これは学生の名前と履修科目の対応が暗黙的なので、言葉による説明が必要となる！==

- 同一学生の名前と履修科目をリストでまとめて管理すると…

``` py title="リストによるグループ化"
students =[['太郎', {'アルゴリズム':5, 'データベース':3}], ['次郎', {'アルゴリズム':4, '人工知能':4}]]
```

==これは学生の名前や履修科目がリストの何番目かを言葉で説明する必要がある！==

## クラスの定義

複数の異なるデータの対応関係を明確にするために**クラス**を使おう。

クラスでまとめられた各変数を**属性**という。

- 名前と履修科目を一塊に扱うことができる
- 名前を格納する変数`name`と、履修科目ごとの成績を格納する変数`classes`を持つ`Student`クラスを定義

``` py title="クラスの定義"
class Student:
    def __init__(self, name, classes):
        self.name = name  # 学生名を格納する属性（name）
        self.classes = classes  # 履修科目とその成績を格納する属性（classes）
```

## インスタンスを作る
クラスから具体的な属性の値を持つオブジェクトを作る。このオブジェクトを**インスタンス**という。

また、インスタンスごとに固有の値を持つ属性のことを**インスタンス変数**という。

- `Student`インスタンスを作ることで、一人の学生の名前と履修科目の関係が明確になる

作り方は以下の通り。

`変数名 = クラス名(インスタンス変数の初期値)`

``` py title="インスタンス生成"
taro = Student('太郎', {'アルゴリズム':5, 'データベース':3})
jiro = Student('次郎', {'アルゴリズム':4, '人工知能':4})
```

## インスタンスの属性にアクセスする
インスタンスの属性値を表示する。

属性へのアクセス方法は以下の通り。

`インスタンス名.属性名`

``` py title="属性の参照"
message = '{}の履修科目は{}です。'
print(message.format(taro.name, '、'.join(taro.classes.keys()))) # keys()で辞書のキーのリストを取得
print(message.format(jiro.name, '、'.join(jiro.classes.keys())))
```

==これは、インスタンスの外のプログラムが、インスタンスの属性を参照して表示している。==

## クラスにメソッドを追加する

自分の属性を使った機能をインスタンス自身に埋め込んだものが**メソッド**。

- 例：`Student`クラスに自己紹介する機能やGPAを計算させる機能を持たせる
- 科目ごとの成績は伝えたくないけど全体のGPAだけなら伝えてもいいというときに便利

メソッド内で自身の属性の値を参照するには`self.属性名`でOK。

``` py title="メソッドの定義"
class Student:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def introduce(self):
        message = '私の名前は{}です。私の履修科目は{}です。'
        print(message.format(self.name, '、'.join(self.classes.keys())))

    def calculateGPA(self):
        gpa = 0
        for grade in self.classes.values():  # values()で辞書の値のリストを取得
            gpa += grade
        return gpa / len(self.classes)  # 成績の平均を返す

taro = Student('太郎', {'アルゴリズム':5, 'データベース':3})
jiro = Student('次郎', {'アルゴリズム':4, '人工知能':4})
```

## メソッドを利用する

メソッドを利用することでインスタンスの属性値を使った処理結果が得られる。

- `introduce`メソッドで`name`属性の値を標準出力
- `calculateGPA`メソッドで`classes`属性の値の平均を返す

!!! info "標準出力と返り値"
    標準出力はターミナル上に文字や数値を表示させるだけで、関数の出力とは別物。  
    試しに`y = print('hello')`というように`print`関数の出力を変数に代入して、その変数に何が代入されるか確認してみよう！

    一方、関数の結果を出力するには`return`を使おう。`return`によって返される出力値のことを**返り値**という。  
    返り値は変数に代入可能なので、==ある関数の結果を他の処理で使いたい場合は、その結果を必ず`return`で返すようにしよう！==

メソッドの利用方法は以下の通り。

`インスタンス名.メソッド名(メソッドの実引数)`

``` py title="メソッド呼び出し"
taro.introduce()
jiro.introduce()
```

==多くのインスタンスのメソッドを利用する場合、このプログラムだと冗長になる。==

### リストを使ってプログラムの冗長な部分をまとめ上げる

同じクラスのインスタンスをリストに格納すると、`for`文を用いることで、同じメソッドを利用するプログラムをまとめて書くことができる。

``` py title="for文による全インスタンスのメソッド呼び出し"
students = [taro, jiro]  # 学生が増えればこのリストの要素を増やすだけ
for student in students:  # この2行は変更不要
    student.introduce()
```

``` py title="全インスタンスのメソッドの返り値を利用"
top_student = students[0]  # 学生リストの先頭を仮の成績トップの学生とする
for student in students[1:]:  # 学生リストの二人目以降と仮の成績トップ学生の成績を比較
    if student.calculateGPA() > top_student.calculateGPA():
        top_student = student  # 仮の成績トップ学生を更新
print('GPAが一番高いのは{}さんで、GPAが{}です。'.format(top_student.name, top_student.calculateGPA()))
```

## 継承を使って同一メソッドの実装を変える

同一メソッドでもインスタンスの種類によって振る舞いを変える。

- `Student`インスタンスはどれも日本語による自己紹介
- 母語に応じて自己紹介の機能を変えたい

機能を作り替えたい場合、親クラスを**継承**して、新しいクラスを作る。このようなクラスのことを**サブクラス**という。

- `Student`クラスを継承して、以下のサブクラスを作る
    - 日本語で自己紹介する`JapaneseStudent`クラス
    - 英語で自己紹介する`EnglishStudent`クラス
    - 中国語で自己紹介する`ChineseStudent`クラス

親クラスを継承してサブクラスを定義する方法は以下の通り。

`class サブクラス名(親クラス名):`

``` py title="サブクラス"
class JapaneseStudent(Student):
    def introduce(self):
        message = '私の名前は{}です。私の履修科目は{}です。'
        print(message.format(self.name, '、'.join(self.classes.keys())))


class EnglishStudent(Student):
    def introduce(self):
        message = 'My name is {}. I take {}.'
        print(message.format(self.name, ', '.join(self.classes.keys())))


class ChineseStudent(Student):
    def introduce(self):
        message = '我叫{}. 我正在学习{}.'
        print(message.format(self.name, '和'.join(self.classes.keys())))


taro = JapaneseStudent('太郎', {'アルゴリズム':5, 'データベース':3})
jiro = JapaneseStudent('次郎', {'アルゴリズム':4, '人工知能':4})
mike = EnglishStudent('Mike', {'Algorithm':3, 'Artificial Intelligence':4})
zhang = ChineseStudent('张', {'编程语言':5, '人工智能':4})
```

## ポリモーフィズムを使う

実装の異なる同一名のメソッドを備えたインスタンスを区別なく利用できることを**ポリモーフィズム**という。

同一名のメソッドを同じように利用しても、各クラスで実装が異なるので、インスタンスに応じて振る舞いを変えることができる。

``` py title="ポリモーフィズム"
students = [taro, jiro, mike, zhang]
for student in students:
    student.introduce()

# 私の名前は太郎です。私の履修科目はアルゴリズム、データベースです。
# 私の名前は次郎です。私の履修科目はアルゴリズム、人工知能です。
# My name is Mike. I take Algorithm, Artificial Intelligence.
# 我叫张. 我正在学习编程语言和人工智能.
```

<!-- ``` py title="ポリモーフィズム"
top_student = students[0]
for student in students[1:]:
    if student.calculateGPA() > top_student.calculateGPA():
        top_student = student
print('GPAが一番高いのは{}さんで、GPAが{}です。'.format(top_student.name, top_student.calculateGPA()))

# GPAが一番高いのは张さんで、GPAが4.5です。
``` -->

- インスタンスごとに自己紹介する言語とデータの言語が一致するのは、データと機能（メソッド）がクラスとして一塊にまとめられているから。
- データと機能を分けて作っていると、「My name is 太郎.」のように異なる言語で組み合わせてしまう危険性がある！
