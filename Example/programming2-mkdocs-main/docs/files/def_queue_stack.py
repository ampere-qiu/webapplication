from def_stop import Stop  # Stopクラスの読み込み


class Stack():
    def __init__(self):
        self.list = []  # データ格納用のインスタンス変数list(リスト)
        self.message = '{}(ID:{})のバス停の緯度経度は({},{})です。'

    def push(self, data):  # スタックにデータをPUSHするメソッド
        if isinstance(data, Stop):  # dataがStopオブジェクトかどうか判定
            self.list.append(data)
        else:
            print('Stopオブジェクト以外はPUSHできません。')

    def pop(self):  # スタックからデータをPOPするメソッド
        if(self.list == []):  # リストが空かどうか判定
            return None
        return self.list.pop()

    def display(self):  # リストを先頭から表示するメソッド
        print('======スタックの底======')
        for i in range(len(self.list)):
            print(self.message.format(self.list[i].name, self.list[i].id, self.list[i].lat, self.list[i].lng))
        print('======スタックの先頭======\n')


class Queue():
    def __init__(self):
        self.list = []  # データ格納用のインスタンス変数list(リスト)
        self.message = '{}(ID:{})のバス停の緯度経度は({},{})です。'

    def enqueue(self, data):  # キューにデータをPUSHするメソッド
        if isinstance(data, Stop):  # dataがStopオブジェクトかどうか判定
            self.list.append(data)
        else:
            print('Stopオブジェクト以外はENQUEUEできません。')

    def dequeue(self):  # キューからデータをDEQUEUEするメソッド
        if(self.list == []):  # リストが空かどうか判定
            return None
        return self.list.pop(0)

    def display(self):  # リストを先頭から表示するメソッド
        print('======キューの先頭======')
        for i in range(len(self.list)):
            print(self.message.format(self.list[i].name, self.list[i].id, self.list[i].lat, self.list[i].lng))
        print('======キューの末尾======\n')
