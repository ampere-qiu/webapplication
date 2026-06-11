# Week 5 (2026/5/15)

!!! abstract "今週の目的"
    再帰呼び出しを用いてデータを検索する。

!!! check "今週のキーワード"
    - 再帰呼び出し
    - 継承

今回はアルゴリズムの実装として、データ列から任意のデータを検索するプログラムを実装する。

具体的には、 ==*先頭から順にデータを探す***線形探索**== と、==*中央値と比較して探索空間を半分割していく***二分探索**== を実装する。なお、線形探索はループを用いたものと再帰呼び出しを用いたものを実装し、二分探索は再帰呼び出しを用いたものを実装する。


## :material-chevron-right:課題1：先頭からデータを検索する
データをリストに格納する`add`メソッドを備えた`DB`クラスを定義せよ。

今回作成する`DB`クラスの仕様は、以下の通りである。

!!! example "DBクラス"
    **`#!python class DB()`**  
    格納したデータを処理（探索・ソート等）するクラス

    **`#!python add(data)`**  
    データを格納するメソッド

    **パラメータ**

    - **data**: 格納するデータ（`Stop`インスタンス）

その後、`DB`クラスを継承した`DBwLinerSearch`クラスを定義し、バス停IDからバス停名を検索する`search`メソッドを実装せよ。なお、`search`メソッドはループを用いた線形探索アルゴリズムで実装すること。

今回作成する`DBwLinerSearch`クラスの仕様は、以下の通りである。

!!! example "DBwLinerSearchクラス"
    **`#!python class DBwLinerSearch()`** *`DB`クラスのサブクラス*  
    格納したデータを線形探索するクラス。

    **`#!python search(query)`**  
    格納したデータを線形探索するメソッド

    **パラメータ**

    - **query**: 探索対象のバス停のID（文字列）

    **返り値**

    - 探索対象のバス停の名前（文字列）

最後に、実装した`DBwLinerSearch`クラスのインスタンスを用いて、`allkyotobus_stop.dat`のデータからIDがED01_1653とED01_4089、ED01_5000のバス停を検索し、バス停名と実行時間を表示せよ。なお、[`allkyotobus_stop.dat`:material-file:](files/allkyotobus_stop.dat){download="allkyotobus_stop.dat"}をダウンロードすること。

=== "プログラム"
    ``` py linenums="1" title="week5_1.py"
    # 穴埋め問題用のプログラム
    from def_stop import Stop # Stopクラスの読み込み
    import time # 実行時間を計測するためのモジュール
    import sys # 再帰呼び出し回数の上限を変更するためのモジュール
    sys.setrecursionlimit(10000) # 再帰呼び出し回数の上限を10000回に変更

    class DB: # DBクラスの定義
        def __init__(self):
            self.list = [] # データを格納するリスト

        def add(self, data):
            self.list.[____](data) # データをリストの末尾に挿入


    class DBwLinerSearch([____]): # 線形探索用のクラス
        def search(self, query):
            for item in self.list: # ループでリストの先頭からチェック
                if item.id == query:
                    return item.name
            return None # ループを抜ければ、探しているデータはなし


    fi = open('allkyotobus_stop.dat', 'r', encoding='utf-8')
    lines = fi.readlines()
    queries = ['ED01_1653', 'ED01_4089', 'ED01_5000']
    db = DBwLinerSearch()
    for line in lines:
        line = line.rstrip()
        items = line.split(' ') # 1行を半角スペースで区切ってitemsリストに代入
        db.[____](Stop(items[0], items[1], float(items[2]), float(items[3]), items[4:])) # StopオブジェクトをDBwLinerSearchのインスタンスに追加
    for query in queries:
        start = time.perf_counter() # 探索前の時間を記録
        result = db.search(query)
        elapsed_time =  time.perf_counter() - [____]  # 探索後の時間から探索前の時間を引き、実行時間を計測
        print("ID:{}は{}です。{}は{}秒かかりました。".format(query, result, db.__class__.__name__, elapsed_time)) # 「オブジェクト名.__class__.__name__」でオブジェクトのクラス名を取得
    fi.close()
    ```

=== "実行例"
    ```
    ID:ED01_1653は府立大学前です。DBwLinerSearchは1.4781951904296875e-05秒かかりました。
    ID:ED01_4089は京都駅前です。DBwLinerSearchは0.00016999244689941406秒かかりました。
    ID:ED01_5000はNoneです。DBwLinerSearchは0.00015616416931152344秒かかりました。
    ```

## :material-chevron-right:課題2：先頭からデータを検索する（再帰）
[課題１](#1)で作成した`DB`クラスを継承した`DBwRecursiveSearch`クラスを定義し、再帰呼び出しを用いて`search`メソッドの線形探索アルゴリズムを実装せよ。具体的には、<u>リストの先頭がクエリと一致しているかどうかを確認し、一致していればバス停名を返し、そうでなければ、2番目以降のデータ列に対して再帰的に検索を行う</u>。

今回作成する`DBwRecursiveSearch`クラスの仕様は、以下の通りである。

!!! example "DBwRecursiveSearchクラス"
    **`#!python class DBwRecursiveSearch()`** *`DB`クラスのサブクラス*  
    格納したデータを再帰呼び出しを用いて線形探索するクラス。

    **`#!python search(query)`**  
    格納したデータを再帰呼び出しを用いて線形探索するメソッド

    **パラメータ**

    - **query**: 探索対象のバス停のID（文字列）

    **返り値**

    - 探索対象のバス停の名前（文字列）

!!! hint "ヒント"
    再帰呼び出し時に引数に与える値を変更しないと、基底ケースにたどり着かなくなり無限ループになることに留意せよ。今回の場合、リストの先頭がクエリと異なっていれば、次に探す空間はリストの2番目以降のデータである。

最後に、実装した`DBwRecursiveSearch`クラスのインスタンスを用いて、`allkyotobus_stop.dat`のデータからIDがED01_1653とED01_4089、ED01_5000のバス停を検索し、バス停名と実行時間を表示せよ。

=== "実行例"
    ```
    ID:ED01_1653は府立大学前です。DBwRecursiveSearchは0.001970052719116211秒かかりました。
    ID:ED01_4089は京都駅前です。DBwRecursiveSearchは0.039069175720214844秒かかりました。
    ID:ED01_5000はNoneです。DBwRecursiveSearchは0.023905038833618164秒かかりました。
    ```

## :material-chevron-right:課題3：二分探索でデータを検索する
[課題１](#1)で作成した`DB`クラスを継承した`DBwBinarySearch`クラスを定義し、再帰呼び出しを用いた二分探索アルゴリズムで`search`メソッドを実装せよ。なお、バス停データのIDは"ED01_"に後続する数字が昇順でソートされていることとする。また、<u>ファイルから読み込んだ時点ではIDが文字列のため、数字の大小を比較するには、スライスを用いて"ED01_"以降の数字を切り出し、`int()`を用いて数値型に変換する必要がある</u>。具体的には`int(list[m].id[5:])`と記述する。

今回作成する`DBwBinarySearch`クラスの仕様は、以下の通りである。

!!! example "DBwBinarySearchクラス"
    **`#!python class DBwBinarySearch()`** *`DB`クラスのサブクラス*  
    格納したデータを二分探索するクラス。

    **`#!python search(query)`**  
    格納したデータを二分探索するメソッド

    **パラメータ**

    - **query**: 探索対象のバス停のID（文字列）

    **返り値**

    - 探索対象のバス停の名前（文字列）

!!! hint "ヒント"
    クエリがリストの中央の要素より大きければ、次に探す空間はリストの後半のデータ列である。一方、クエリがリストの中央の要素より小さければ、次に探す空間はリストの前半のデータ列である。

最後に、これまで実装した`DBwLinerSearch`クラス、`DBwRecursiveSearch`クラス、`DBwBinarySearch`クラスの各インスタンスを用いて、`allkyotobus_stop.dat`のデータからIDがED01_1653とED01_4089、ED01_5000のバス停を検索し、バス停名と実行時間を表示せよ。本課題は、実装が異なると実行速度が変わることを理解することが目的である。

=== "実行例"
    ```
    ID:ED01_1653は府立大学前です。DBwLinerSearchは1.0013580322265625e-05秒かかりました。
    ID:ED01_4089は京都駅前です。DBwLinerSearchは0.000102996826171875秒かかりました。
    ID:ED01_5000はNoneです。DBwLinerSearchは0.0001780986785888672秒かかりました。
    ID:ED01_1653は府立大学前です。DBwRecursiveSearchは0.001550912857055664秒かかりました。
    ID:ED01_4089は京都駅前です。DBwRecursiveSearchは0.041697025299072266秒かかりました。
    ID:ED01_5000はNoneです。DBwRecursiveSearchは0.02522110939025879秒かかりました。
    ID:ED01_1653は府立大学前です。DBwBinarySearchは2.5033950805664062e-05秒かかりました。
    ID:ED01_4089は京都駅前です。DBwBinarySearchは0.00015163421630859375秒かかりました。
    ID:ED01_5000はNoneです。DBwBinarySearchは1.4781951904296875e-05秒かかりました。
    ```
