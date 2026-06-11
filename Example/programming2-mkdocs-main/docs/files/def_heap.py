class Heap:  # Heapクラスの定義
    def __init__(self):
        self.list = [0]  # データを格納するリスト。0番目の要素は使わないため0を代入。
        self.size = 0

    def insert(self, data):
        self.list.append(data)  # データをヒープの最後の要素の次に挿入
        self.size += 1  # ヒープサイズを1増やす
        self.shift_up(self.size)  # 挿入した要素をシフトアップする

    def shift_up(self, num):  # num番目の要素をシフトアップ
        # num番目の要素が根でなく、num番目の要素の親の方が大きい場合、親子を入れ替え
        if num > 1 and self.list[num//2].lng > self.list[num].lng:
            self.list[num], self.list[num//2] = self.list[num//2], self.list[num]
            self.shift_up(num//2)  # 入れ替え後に、引き続き新しい親のシフトアップ

    def show_tree(self, num):  # num番目の要素を根とする木（もしくは部分木）を表示するメソッド
        if num <= self.size:  # 要素numがヒープサイズの範囲内である限り
            self.show_tree(2*num+1)  # 要素numの右子を根とする部分木を表示
            i = num
            space = ''
            while i // 2 > 0:  # 要素numの深さ分だけ半角スペース2個を連結
                space += '  '
                i = i // 2
            # 連結されたタブ（インデント）と要素numのバス停の名前と緯度を表示
            print('{}{}:{}'.format(
                space, self.list[num].name, self.list[num].lng))
            self.show_tree(2*num)  # 要素numの左子を根とする部分木を表示

    def is_heap(self):  # ヒープ条件のチェック
        for i in range(self.size, 1, -1):
            if self.list[i].lng < self.list[i//2].lng:
                return False
        return True

    def delete_min(self):
        if self.size > 0:
            min = self.list.pop(1)  # ヒープの根を切り取り、最小値の変数に代入する
            self.size -= 1  # ヒープサイズを１減らす
            self.list.insert(1, self.list.pop())  # ヒープの最後尾を切り取り、根に挿入する
            self.shift_down(1)  # 挿入された根を適切な位置まで下げる（シフトダウン）
            return min  # ヒープの最小値を返す
        else:
            return None

    def shift_down(self, num):
        index = self.min_child(num)  # 要素numの子供のうち最小の子供のインデックスを取得する
        if num <= self.size and self.list[num].lng > self.list[index].lng:
            # 最小の子供の方が要素numよりも小さく、num番目がヒープサイズを超えていない場合、
            # 最小の子供と要素numを入れ替える
            self.list[num], self.list[index] = self.list[index], self.list[num]
            self.shift_down(index)  # 入れ替え後に、新しい子供のシフトダウン

    def min_child(self, num):
        if 2*num > self.size:  # 要素numに子供がいなければ、要素numを返す
            return num
        elif 2*num+1 > self.size:  # 要素numに左子しかいなければ、左子のindexを返す
            return 2*num
        # 要素numの左子の方が右子より小さい場合、左子のindexを返す
        elif self.list[2*num].lng < self.list[2*num+1].lng:
            return 2*num
        else:  # 要素numの右子の方が左子より小さい場合、右子のindexを返す
            return 2*num+1

    def build_heap(self, list):
        self.list.extend(list)
        self.size = len(list)
        num = self.size//2  # リストの中央のnumを取得する
        while num > 0:  # numがヒープの節の範囲内である限り
            self.shift_down(num)
            num -= 1  # 要素numを左隣（num-1）の要素に更新
