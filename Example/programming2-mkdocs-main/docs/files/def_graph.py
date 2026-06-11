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
        if id not in self.node_list:  # ノードリストにidのノードが無ければ
            self.node_list[id] = []  # ノードリストにidのノードを追加する．ただし、近傍はないので[]を代入
            self.num_nodes += 1  # ノードの数をインクリメント

    def add_directed_edge(self, sid, tid, label):  # グラフに有向エッジを追加するメソッド
        if sid not in self.node_list:  # 始点のノードが無ければ追加
            self.add_node(sid)
        if tid not in self.node_list:  # 終点のノードが無ければ追加
            self.add_node(tid)
        self.node_list[sid].insert(0, Neighbor(tid, label))  # 近傍リストに終点のノードを追加
        self.num_edges += 1  # エッジの数をインクリメント

    def add_undirected_edge(self, sid, tid, label):  # グラフに無向エッジを追加するメソッド
        self.add_directed_edge(sid, tid, label)  # 両方向にエッジを追加
        self.add_directed_edge(tid, sid, label)
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

    def remove_directed_edge(self, sid, tid, label = None): # 有向エッジを削除するメソッド
        if sid in self.node_list and tid in self.node_list: # 始点ノードと終点ノードがあれば
            neighborhood = [] # 削除後の近傍リスト
            for neighbor in self.get_neighborhood(sid):
                if neighbor.id == tid and (neighbor.label == label or label == None): # 隣接ノードが終点ノードかつラベルが等しければ
                    self.num_edges -= 1 # エッジの総数を一本減らす
                else:
                    neighborhood.append(neighbor) # 削除後の近傍リストに追加
            self.node_list[sid] = neighborhood # 近傍リストを更新

    def remove_undirected_edge(self, sid, tid, label = None): # 無向エッジを削除するメソッド
        edges = self.num_edges
        self.remove_directed_edge(sid, tid, label)  # 一方向のエッジを削除
        removed_edges = edges - self.num_edges  # 削除した一方向のエッジの数を求める
        self.remove_directed_edge(tid, sid, label)  # 逆方向のエッジを削除
        self.num_edges += removed_edges  # エッジを重複して削除したのでエッジの数をインクリメント

    def remove_node(self, id): # ノードを削除するメソッド
        if id in self.node_list:
            for node in self.get_node_list(): # 削除対象のノード以外のノードに対して
                if node != id:
                    self.remove_directed_edge(node, id) # 削除対象のノードに接続するエッジを削除
            self.node_list.pop(id) # 削除対象のノードをノードリストから削除
            self.num_nodes -= 1 # ノード数をデクリメント
