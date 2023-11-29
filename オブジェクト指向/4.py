class Bird:
    #コンストラクタの引数がnameなのでBirdクラスの引数もname
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The bird named {} is flying".format(self.name))


class Dog:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The dog named {} is running".format(self.name))


class Fish:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The fish named {} is swimming".format(self.name))
#インスタンスを作成
bob = Bird("Bob")
john = Bird("John")
david = Dog("David")
fabian = Fish("Fabian")
#全てのインスタンスのmoveメソッドを呼び出す
bob.move()
john.move()
david.move()
fabian.move()