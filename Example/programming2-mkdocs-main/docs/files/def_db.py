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

    def is_sorted(self):
        for i in range(self.count()-1):
            if self.list[i].lng > self.list[i+1].lng:
                return False
        return True
