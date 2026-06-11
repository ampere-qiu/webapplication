# Week 6 (2026/5/22)

!!! abstract "今週の目的"
    データを昇順・降順に並べ替える。

!!! check "今週のキーワード"
    - 二重ループ
    - 値の入れ換え（スワップ）
    - バブルソート、選択法、挿入法

今回はアルゴリズムの実装として、データ列を並べ替える（ソート）プログラムを実装する。

具体的には、隣同士を比較して入れ替えていく**バブルソート**、最小値もしくは最大値を見つけて左端と入れ替える**選択法**、整列済みのデータ列にデータを挿入していく**挿入法**を実装する。

## :material-chevron-right:課題1：データを並べ替える（バブルソート）
データをリストに格納する`add`メソッドと、そのリストを表示する`display`メソッド、リストの件数を返す`count`メソッド、データを昇順に並べ替える`sort`メソッド、データが昇順にソートされているか確認する`is_sorted`メソッドを備えた`DB`クラス（親クラス）を定義せよ。

`DB`クラスの仕様は、以下の通りである。

!!! example "DBクラス"
    **`#!python class DB()`**  
    格納したデータを並べ替えるクラス

    **インスタンス変数**

    - **list**: データ格納用のリスト

    **`#!python add(data)`**  
    データをリストに格納するメソッド

    **パラメータ**

    - **data**: 格納するデータ（`Stop`インスタンス）

    **`#!python display()`**  
    リストの中身を表示するメソッド

    **`#!python count()`**  
    リストの件数を数えるメソッド

    **返り値**

    - リストに格納されていたデータの件数を返す（整数）

    **`#!python sort()`**  
    リストの中身を昇順に並べ替えるメソッド

    **`#!python is_sorted()`**  
    リストの中身が昇順に並んでいるか確認するメソッド

    **返り値**

    - データが昇順に並んでいれば`True`、そうでなければ`False`を返す（ブール値）


その後、`DB`クラスを継承した`DBwBubbleSort`クラス（子クラス）を定義し、`sort`メソッドを「バブルソートアルゴリズム」で実装せよ。

`DBwBubbleSort`クラスの仕様は、以下の通りである。

!!! example "DBwBubbleSortクラス"
    **`#!python class DBwBubbleSort()`** *`DB`クラスのサブクラス*  
    格納したデータをバブルソートで並べ替えるクラス

    **`#!python sort()`**  
    リストの中身をバブルソートで昇順に並べ替えるメソッド

最後に、実装した`DBwBubbleSort`クラスのインスタンスを用いて、`allkyotobus_stop.dat`のデータをバス停の経度の小さい順（西から東に）に並べ替えて、その結果と実行時間を表示せよ。

=== "プログラム"
    ``` py linenums="1" title="week6_1.py"
    # 穴埋め問題用のプログラム
    from def_stop import Stop  # Stopクラスの読み込み
    import time  # 実行時間を計測するためのモジュール


    class DB:  # DBクラスの定義
        def __init__(self):
            self.list = []  # データを格納するリスト

        def add(self, data):
            self.list.append(data)  # データをリストの末尾に挿入

        def display(self):
            message = '{}: {}(ID:{})のバス停の緯度経度は({},{})です。'
            j = 1
            for i in self.list:
                print(message.format(j, i.name, i.id, i.lat, i.lng))
                j += 1

        def count(self):  # データの件数を返す
            return len(self.list)

        def sort(self):  # データを昇順にソートする
            pass

        def is_sorted(self, descent = False):  # 降順の場合は引数にTrue
            for i in range(self.count()-1):
                if not descent and (self.list[i].lng > self.list[i+1].lng or self.list[i].id == self.list[i+1].id):
                    return False
                elif descent and (self.list[i].lng < self.list[i+1].lng or self.list[i].id == self.list[i+1].id):
                    return False
            return True


    class DBwBubbleSort(DB):  # バブルソート用のクラス
        def sort(self):
            n = self.count()  # データ件数を取得
            for i in range([____], 0, [____]):  # 右端から順に2番目の要素まで最大値を確定させていく
                for j in range([____]):  # 左端から順に比較＆入換えを繰り返す
                    if self.list[j].lng > self.list[j+1].lng:  # 左側の方が大きい場合
                        self.list[j], self.list[j+1] = self.list[j+1], self.list[j]  # スワップ

    if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
        fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
        lines = fi.readlines()
        db = DBwBubbleSort()
        for line in lines:
            line = line.rstrip()
            items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
            db.[____](Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:]))  # Stopインスタンスをdbに追加
        start = time.time()  # ソート前の時間を記録（time()は現在時刻を返すメソッド）
        db.[____]  # データのソートを実行
        elapsed_time = time.time() - start  # ソート後の時間からソート前の時間を引き、実行時間を計測
        db.display()
        if db.is_sorted():
            print("ソートが完了しました！{}は{}秒かかりました。".format(db.__class__.__name__, elapsed_time))  # __class__はインスタンスのクラスを返し、__name__はそのクラスの名前を返す
        fi.close()
    ```

=== "実行例"
    ```
    1: 下夜久野駅前(ID:ED01_85)のバス停の緯度経度は(35.32033486,134.99883496)です。
    2: 畑口(ID:ED01_86)のバス停の緯度経度は(35.32009052,135.00174923)です。
    （中略）
    1849: 自治会館前(ID:ED01_2850)のバス停の緯度経度は(34.86017838,135.89218112)です。
    1850: 緑苑坂東(ID:ED01_2851)のバス停の緯度経度は(34.86244101,135.89352647)です。
    ソートが完了しました！DBwBubbleSortは1.0563509464263916秒かかりました。
    ```

!!! info "if \__name__ == '\__main__':とは？"
    プログラムで定義されたクラス（たとえば`DB`クラス）や関数を他のプログラムにインポートすると、インポートしたクラスや関数だけでなく、==そのプログラム全体が読み込まれ実行されます。==

    クラス定義や関数定義のみ書かれたプログラムであれば問題ありませんが、それらを使った処理まで書かれていると、それらが実行されてしまいます。たとえば、`week7_1.py`の`DB`クラスのみをインポート（`from week7_1 import DB`）して、`DB`クラスを継承した`DBwSelectSort`クラスを実装しようとすると、`DBwBubbleSort`インスタンスを生成して、データを追加しソートして結果を表示する処理も実行されるわけです。

    プログラムをモジュールとしてインポートしている（`from week7_1 import DB`）のか、プログラムを直接実行している（`python week7_1.py`）のかを区別するために`__name__`という特殊なグローバル変数があります。`__name__`の値がモジュール名の場合（`week7_1`）は、インポートしているときの実行を表し、`__name__`の値が`'main'`の場合は、プログラムを直接実行していることを表しています。

    したがって、`#!python if __name__ == '__main__':`と書くと、そのプログラムがモジュールとして他のプログラムにインポートされたときに、`#!python if __name__ == '__main__':`以下の処理をスキップすることができます。

## :material-chevron-right:課題2：データを並べ替える（選択ソート）
[課題1](#1)で作成したDBクラス（親クラス）を継承した`DBwSelectSort`クラス（子クラス）を定義し、`sort`メソッドを「選択ソートアルゴリズム」で実装せよ。

`DBwSelectSort`クラスの仕様は、以下の通りである。

!!! example "DBwSelectSortクラス"
    **`#!python class DBwSelectSort()`** *`DB`クラスのサブクラス*  
    格納したデータを選択ソートで並べ替えるクラス

    **`#!python sort()`**  
    リストの中身を選択ソートで昇順に並べ替えるメソッド

最後に、実装した`DBwSelectSort`クラスのインスタンスを用いて、`allkyotobus_stop.dat`のデータをバス停の経度の小さい順（西から東に）に並べ替えて、その結果と実行時間を表示せよ。

=== "実行例"
    ```
    1: 下夜久野駅前(ID:ED01_85)のバス停の緯度経度は(35.32033486,134.99883496)です。
    2: 畑口(ID:ED01_86)のバス停の緯度経度は(35.32009052,135.00174923)です。
    （中略）
    1849: 自治会館前(ID:ED01_2850)のバス停の緯度経度は(34.86017838,135.89218112)です。
    1850: 緑苑坂東(ID:ED01_2851)のバス停の緯度経度は(34.86244101,135.89352647)です。
    ソートが完了しました！DBwSelectSortは0.7865409851074219秒かかりました。
    ```

## :material-chevron-right:課題3：データを並べ替える（挿入ソート）
[課題1](#1)で作成した`DB`クラス（親クラス）を継承した`DBwInsertSort`クラス（子クラス）を定義し、`sort`メソッドを挿入ソートアルゴリズムで実装せよ。

`DBwInsertSort`クラスの仕様は、以下の通りである。

!!! example "DBwInsertSortクラス"
    **`#!python class DBwInsertSort()`** *`DB`クラスのサブクラス*  
    格納したデータを挿入ソートで並べ替えるクラス

    **`#!python sort()`**  
    リストの中身を挿入ソートで昇順に並べ替えるメソッド

最後に、これまで実装した`DBwBubbleSort`クラス、`DBwSelectSort`クラス、`DBwInsertSort`クラスの各インスタンスを用いて、`allkyotobus_stop.dat`のデータをバス停の経度の小さい順（西から東に）に並べ替えて、その実行時間を表示せよ。本課題は、実装が異なると実行速度が変わることを理解することが目的である。

=== "実行例"
    ```
    ソートが完了しました！DBwBubbleSortは1.0725622177124023秒かかりました。
    ソートが完了しました！DBwSelectSortは0.8025329113006592秒かかりました。
    ソートが完了しました！DBwInsertSortは0.449016809463501秒かかりました。
    ```
