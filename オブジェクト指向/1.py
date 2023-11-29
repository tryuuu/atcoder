class SimpleData:

    a = 0
    b = 0

    def sum(self):
        return self.a + self.b

    def set(self, a, b):
        self.a = a
        self.b = b
        
#data1はインスタンス変数
data1=SimpleData()#classのインスタンス化
data1.set(1,2)
print(data1.sum())