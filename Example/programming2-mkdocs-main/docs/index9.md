# Week 9 (2025/6/20)

!!! abstract "今週の目的"
    データをグラフに格納する。

!!! check "今週のキーワード"
    - グラフのデータ構造（エッジリスト、隣接リスト）
    - 開放除去（エッジの削除）
    - 点の除去

今回はグラフのデータ構造の一つである隣接リストを実装する。 ==**隣接リスト**とは、各ノードの近傍をリストとして表現したデータ構造である。== ==**近傍**とは同じノードに隣接するノード（以降、**隣接ノード**）の集合である。== 隣接リストでは、各ノードの近傍を隣接ノードとそれに接続するエッジのペアのリストとして表現する。

## :material-chevron-right:課題1：グラフを作る
隣接リストのデータ構造を実装した`Graph`クラスを定義せよ。なお、グラフの各ノードの近傍は、隣接ノードとそれに接続するエッジからなる`Neighbor`インスタンスのリストで実装する。また、全てのノードの近傍をまとめるのに辞書（キーがノードID、値が近傍）を用いよ。

`Graph`クラスと`Neighbor`クラスの仕様は、以下の通りである。

!!! example "Graphクラス"
    **`#!python class Graph()`**  
    隣接リストで実装したグラフのクラス

    **インスタンス変数**

    - **node_list**: グラフ上のノードリスト(辞書：key=ノードID（文字列）, value=近傍（`Neighbor`インスタンスのリスト）)
    - **num_nodes**: グラフ上のノード数（整数）
    - **num_edges**: グラフ上のエッジ数（整数）

    **`#!python add_node(id)`**  
    グラフにノードを追加するメソッド

    **パラメータ**

    - **id**: 追加するノードのID（文字列）

    **`#!python add_directed_edge(sid, tid, label)`**  
    ノード`sid`からノード`tid`にラベル`label`付きの有向エッジを追加するメソッド

    **パラメータ**

    - **sid**: 追加するエッジの始点のノードID（文字列）
    - **tid**: 追加するエッジの終点のノードID（文字列）
    - **label**: 追加するエッジのラベル（文字列）

    **`#!python add_undirected_edge(sid, tid, label)`**  
    ノード`sid`とノード`tid`にラベル`label`付きの無向エッジを追加するメソッド

    **パラメータ**

    - **sid**: 追加するエッジの一端のノードID（文字列）
    - **tid**: 追加するエッジの他端のノードID（文字列）
    - **label**: 追加するエッジのラベル（文字列）

    **`#!python get_node_list()`**  
    グラフのノードリストを返すメソッド

    **返り値**

    - ノードリストを返す（辞書：key=ノードID（文字列）, value=近傍（`Neighbor`インスタンスのリスト））

    **`#!python get_neighborhood(id)`**  
    ノード`id`の近傍を返すメソッド

    **パラメータ**

    - **id**: 近傍取得の対象となるノードID（文字列）

    **返り値**

    - 近傍を返す（`Neighbor`インスタンスのリスト）ただし、指定した`id`のノードが無ければ`None`を返す

    **`#!python get_num_nodes()`**  
    グラフのノード数を返すメソッド

    **返り値**

    - ノード数を返す（整数）

    **`#!python get_num_edges()`**  
    グラフのエッジ数を返すメソッド

    **返り値**

    - エッジ数を返す（整数）

    **`#!python print_graph()`**  
    グラフの隣接関係を表示するメソッド

!!! example "Neighborクラス"
    **`#!python class Neighbor()`**  
    隣接ノードのクラス

    **インスタンス変数**

    - **id**: 隣接ノードのID（文字列）
    - **label**: 隣接ノードと接続するエッジのラベル

さらに、実装した`Graph`クラスのインスタンスを用いて、[`kyotocitybus_line.dat`:material-file:](files/kyotocitybus_line.dat){download="kyotocitybus_line.dat"}のデータを読み込み、グラフを生成せよ。`kyotocitybus_line.dat`は、「バス停ID バス停ID 京都市 路線名」のフォーマットで表されたエッジリストである。

=== "プログラム"
    ``` py linenums="1" title="week9_1.py"
    # 穴埋め問題用のプログラム
    class Neighbor:
        def __init__(self, id, label):
            self.id = id  # 隣接ノードのID
            self.label = label  # 隣接ノードと接続するエッジのラベル

    class Graph:
        def __init__(self):
            self.node_list = {}  # グラフ上のノードリスト(辞書：key=ノードID, value=近傍)
            self.num_nodes = 0  # グラフ上のノードの数
            self.num_edges = 0  # グラフ上のエッジの数

        def add_node(self, id):  # グラフにノードを追加するメソッド
            if id not in [____]:  # ノードリストにidのノードが無ければ
                self.node_list[id] = []  # ノードリストにidのノードを追加する．ただし、近傍はないので[]を代入
                self.num_nodes += 1  # ノードの数をインクリメント

        def add_directed_edge(self, sid, tid, label):  # グラフに有向エッジを追加するメソッド
            if sid not in self.node_list:  # 始点のノードが無ければ追加
                self.add_node([____])
            if tid not in self.node_list:  # 終点のノードが無ければ追加
                self.add_node([____])
            self.node_list[[____]].insert(0, Neighbor([____], label))  # 近傍リストに終点のノードを追加
            self.num_edges += 1  # エッジの数をインクリメント

        def add_undirected_edge(self, sid, tid, label):  # グラフに無向エッジを追加するメソッド
            self.add_directed_edge([____], [____], label)  # 両方向にエッジを追加
            self.add_directed_edge([____], [____], label)
            self.num_edges -= 1  # エッジの数が重複するのでデクリメント

        def get_node_list(self):
            return self.node_list

        def get_neighborhood(self, id):
            if id in self.node_list:
                return self.node_list[id]
            else:
                return None

        def get_num_nodes(self):
            return self.num_nodes

        def get_num_edges(self):
            return self.num_edges

        def print_graph(self):  # 隣接リストを表示するメソッド
            for id in self.get_node_list():
                for neighbor in self.get_neighborhood(id):
                    print('{} is connected to {} by {}.'.format(id, neighbor.id, neighbor.label))

    if __name__ == '__main__':  # モジュールとしてインポートされるときは実行しない
        fi = open('kyotocitybus_line.dat', 'r', encoding = 'utf-8')
        bus_network = Graph()
        lines = fi.readlines()
        for line in lines:
            line = line.rstrip()
            items = line.split(' ')  # 1行を半角スペースで区切ってitemsリストに代入
            bus_network.add_undirected_edge(items[0], items[1], items[3])  # 無向エッジを追加
        print('ノード(バス停)の数は{}個'.format(bus_network.get_num_nodes()))
        print('エッジ(バス停間のリンク)の数は{}個'.format(bus_network.get_num_edges()))
        bus_network.print_graph()
        fi.close()
    ```

=== "実行例"
    ```
    ノード(バス停)の数は667個
    エッジ(バス停間のリンク)の数は2307個
    ED01_1914 is connected to ED01_1925 by M1号系統.
    ED01_1914 is connected to ED01_1936 by 快速205号系統.
    （中略）
    ED01_1909 is connected to ED01_1741 by 11号系統.
    ED01_1909 is connected to ED01_1750 by 11号系統.
    ```

## :material-chevron-right:課題2：グラフのエッジを削除する
[課題1](#1)で作成した`Graph`クラスに、グラフのエッジを削除する`remove_undirected_edge`メソッドを定義せよ。なお、グラフのエッジは両端のノードとラベルで一意に定まるとする。ラベルが`None`の場合は、指定した両端のノードの間のエッジを全て削除すること。

`Graph`クラスの`remove_undirected_edge`メソッドの仕様は、以下の通りである。

!!! example "remove_undirected_edgeメソッド"
    **`#!python remove_undirected_edge(sid, tid, label = None)`**  
    グラフからノード`sid`とノード`tid`の間のエッジを削除するメソッド

    **パラメータ**

    - **sid**: 削除するエッジの一端のノードID（文字列）
    - **tid**: 削除するエッジの他端のノードID（文字列）
    - **label**: 削除するエッジのラベル．省略可（文字列）

さらに、[課題１](#1)で`kyotocitybus_line.dat`のデータを読み込んだ`Graph`インスタンスから、ED01_1914とED01_1925間でM1号系統のラベルが付与されたエッジを`remove_undirected_edge`メソッドで削除せよ。

!!!hint "ヒント"
    [課題１](#1)で作成したグラフは<u>無向グラフのため、両向きのエッジ（始点と終点が逆のもの）が存在するので両方とも削除すること。</u>具体的には、指定した始点のノードの近傍から終点のノードを削除するだけでなく、終点のノードの近傍から始点のノードも削除すること。

=== "実行例"
    ```
    ノード(バス停)の数は667個
    エッジ(バス停間のリンク)の数は2306個
    ED01_1914 is connected to ED01_1936 by 快速205号系統.
    ED01_1914 is connected to ED01_1936 by 快速202号系統.
    （中略）
    ED01_1909 is connected to ED01_1741 by 11号系統.
    ED01_1909 is connected to ED01_1750 by 11号系統.
    ```

## :material-chevron-right:課題3：グラフのノードを削除する
[課題1](#1)で作成した`Graph`クラスに、グラフのノードを削除する`remove_node`メソッドを定義せよ。
なお、グラフのノードはノードIDで一意に定まるとする。

`Graph`クラスの`remove_node`メソッドの仕様は、以下の通りである。

!!! example "remove_nodeメソッド"
    **`#!python remove_node(id)`**  
    グラフからノード`id`を削除するメソッド

    **パラメータ**

    - **id**: 削除するノードのノードID（文字列）

さらに、[課題1](#1)で`kyotocitybus_line.dat`のデータを読み込んだ`Graph`インスタンスから、ED01_1914のノードを`remove_node`メソッドで削除せよ。

!!!hint "ヒント"
    <u>ノードの削除だけでなく、接続しているエッジも全て削除しなければならないことに注意せよ。</u>具体的には、ノードリストから指定したノードIDに対応する要素を削除するだけでなく、隣接ノードの近傍内の当該ノードも削除すること。

=== "実行例"
    ```
    ノード(バス停)の数は666個
    エッジ(バス停間のリンク)の数は2297個
    ED01_1915 is connected to ED01_1916 by 59号系統.
    ED01_1915 is connected to ED01_1916 by 12号系統.
    （中略）
    ED01_1909 is connected to ED01_1741 by 11号系統.
    ED01_1909 is connected to ED01_1750 by 11号系統.
    ```
