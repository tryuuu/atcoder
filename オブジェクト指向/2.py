class SimpleData:
    #コンストラクタを作成(インスタンス化されたときに最初に呼ばれる特別なメソッド)
    def __init__(self):
        self.a = 0
        self.b = 0

    def sum(self):
        return self.a + self.b

    def set(self, a, b):
        self.a = a
        self.b = b

data1 = SimpleData()
print(data1.sum())
#print(data1.sum(1,2))だとエラー