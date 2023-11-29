class Person:
    #カプセル化(複数データを束ねる)
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def describe(self):
        print("name: {}; age: {}; height: {}".format(self.name, self.age, self.height))

    def introduce(self):
        print("My name is {}, and height is {}, and age is {}. ".format(self.name, self.height, self.age))

#インスタンス化
bob = Person("Bob", 24, 170)
mary = Person("Mary", 10, 160)
#メソッド呼び出し
bob.describe()
bob.introduce()
mary.describe()
mary.introduce()