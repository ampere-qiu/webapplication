# Nodeクラスの定義
class Node:
    def __init__(self, data, next = None):  # nextにデフォルト値（何も値が渡されなかった時に設定される値）を設定
        self.data = data  # データを格納するインスタンス変数
        self.next = next  # 連結される次の節を指すインスタンス変数
