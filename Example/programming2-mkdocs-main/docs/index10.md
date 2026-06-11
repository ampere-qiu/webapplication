# Week 10 (2025/6/27)

!!! abstract "今週の目的"
    グラフ上のノードをたどる。

!!! check "今週のキーワード"
    - グラフ上のウォーク（歩道）

今回はグラフの探索の準備として、隣接ノードを辿るプログラムを実装する。

## :material-chevron-right:課題1：グラフ上を歩く
[前回](index10.md#1)実装した`Graph`クラスを継承し、隣接ノードを辿る以下の`walk(start, step)`メソッドを備えた`GraphWalk`クラス定義せよ。ただし、訪問先のノードは近傍リストの先頭のノードとする。

なお、`Graph`クラスは[`def_graph.py`:material-file:](files/def_graph.py){download="def_graph.py"}モジュールの`Graph`クラスをインポートして用いること。

`GraphWalk`クラスの仕様は、以下の通りである。

!!! example "GraphWalkクラス"
    **`#!python class GraphWalk()`** *`Graph`クラスのサブクラス*  
    グラフ上のノードを辿ることができるクラス

    **`#!python walk(start, step)`**  
    指定されたノードから指定された数だけグラフ上のノードを辿る（ウォーク）メソッド

    **パラメータ**

    - **start**: ウォークの開始ノードのID（文字列）
    - **step**: 辿る隣接ノードの数（整数）

次に、前回と同じ[`kyotocitybus_line.dat`:material-file:](files/kyotocitybus_line.dat){download="kyotocitybus_line.dat"}のデータを読み込んだ`GraphWalk`インスタンスを用いて、`ED01_1914`から`5ステップ`分進むパスを出力せよ。なお、`kyotocitybus_line.dat`は、「バス停ID バス停ID 京都市 路線名」のフォーマットで表されたエッジリストである。

=== "プログラム"
    ``` py linenums="1" title="week10_1.py"
    # 穴埋め問題用のプログラム
    from def_graph import Graph  # Graphクラスの読み込み

    class GraphWalk(Graph):
        def walk(self, start, step):
            visited = [start]  # 開始地点のノードIDを訪問済みリストに追加
            parents = {start:None}  # 直前のノードとそれに接続するエッジのペア（タプル）を格納する辞書（key=訪問中ノードID、value=(直前のノードID, エッジラベル)）
            current = start  # 開始地点のノードIDを探索基点のノードに設定
            for i in range(step):  # step分、訪問を繰り返す
                if current not in self.node_list:  # 訪問中ノードが存在しなければ
                    print('{}のノードがグラフ上に存在しません。'.format(current))
                    return
                neighbors = self.get_neighborhood([____])  # 訪問中ノードの隣接ノードを取得
                if neighbors != []:  # 隣接ノードがあれば以下を実行
                    visited.append(neighbors[0].id)  # 次の訪問先を訪問する
                    parents[[____]] = ([____], neighbors[0].label)  # 訪問中ノードIDとそれに接続するエッジをparents辞書に追加
                    current = [____]  # 訪問先候補を次の訪問先に決定
                else:  # 隣接ノードが無ければ終了
                    print('{}から{}ステップ分進むパスはありません。'.format(start, step))
                    return
            # 訪問したノードを訪問順に表示する
            path = visited[0]  # 最初に訪問したノードをpathに代入
            for v in visited[1:]:  # 訪問した順にノードを取得
                path = path + ' --[' + parents[v][1] +']--> ' + v  # 次の訪問先と辿ったエッジをpathに連結
            print(path)


    if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
        fi = open('kyotocitybus_line.dat', 'r', encoding = 'utf-8')
        bus_network = GraphWalk()
        lines = fi.readlines()
        for line in lines:
            line = line.rstrip()
            items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
            bus_network.add_undirected_edge(items[0], items[1], items[3])  # 無向エッジを追加
        bus_network.walk('ED01_1914', 5)
        fi.close()
    ```

=== "実行例"
    ```
    ED01_1914 --[快速202号系統]--> ED01_1936 --[快速202号系統]--> ED01_1914 --[快速202号系統]--> ED01_1936 --[快速202号系統]--> ED01_1914 --[快速202号系統]--> ED01_1936
    ```

## :material-chevron-right:課題2：グラフ上を巡回せずに歩く
[課題1](#1)で作成した`walk(start, step)`メソッドを改良し、訪問済みのノードの再訪を避ける、以下の`walk_without_loop(start, step)`メソッドを定義せよ。

`GraphWalk`クラスの`walk_without_loop`メソッドの仕様は、以下の通りである。

!!! example "walk_without_loopメソッド"
    **`#!python walk_without_loop(start, step)`**  
    指定されたノードから指定された数だけグラフ上の未訪問のノードを辿る（ウォーク）メソッド

    **パラメータ**

    - **start**: ウォークの開始ノードのID（文字列）
    - **step**: 辿る隣接ノードの数（整数）

次に、`kyotocitybus_line.dat`のデータを読み込んだ`GraphWalk`インスタンスを用いて、`ED01_1914`からループせずに`5ステップ`分進むパスを出力せよ。課題1と結果が異なることに注意せよ。

=== "実行例"
    ```
    ED01_1914 --[快速202号系統]--> ED01_1936 --[快速202号系統]--> ED01_1927 --[快速202号系統]--> ED01_1883 --[10号系統]--> ED01_1882 --[10号系統]--> ED01_1881
    ```

## :material-chevron-right:課題3：グラフ上の指定された道を歩く
[課題1](#1)で作成した`walk(start, step)`メソッドを改良し、指定したラベルのエッジを辿る、以下の`walk_along_route(start, step, route)`メソッドを定義せよ。

`GraphWalk`クラスの`walk_along_route`メソッドの仕様は、以下の通りである。

!!! example "walk_along_routeメソッド"
    **`#!python walk_along_route(start, step, route)`**  
    指定されたノードから指定された数だけ、グラフ上の指定されたラベルに接続するノードを辿る（ウォーク）メソッド

    **パラメータ**

    - **start**: ウォークの開始ノードのID（文字列）
    - **step**: 辿る隣接ノードの数（整数）
    - **label**: 隣接ノードに接続するエッジのラベル（文字列）

次に、`kyotocitybus_line.dat`のデータを読み込んだ`GraphWalk`インスタンスを用いて、ED01_1914から5ステップ分進む快速202号系統のパスを出力せよ。余力があれば、`kyotocitybus_stop.dat`のデータも読み込み、バス停IDをバス停名に変換して表示せよ。

=== "実行例"
    ```
    ED01_1914 --[快速202号系統]--> ED01_1936 --[快速202号系統]--> ED01_1927 --[快速202号系統]--> ED01_1883 --[快速202号系統]--> ED01_1930 --[快速202号系統]--> ED01_1742
    ```
