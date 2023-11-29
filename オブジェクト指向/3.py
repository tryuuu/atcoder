class SimpleData:

    def __init__(self):
        self.a = 0
        self.b = 0
#このようなコンストラクタを作るとSimpleDataの引数は二つになる
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def set(self, a, b):
        self.a = a
        self.b = b
#同じ名前のメソッドが複数定義されている場合、最後に定義されたメソッドが優先される
#なのでdata1 = SimpleData()はエラー
data1 = SimpleData(1,2)
print(data1.sum())
