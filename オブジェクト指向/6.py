#オブジェクトの動的操作
class Individual:
    #初期値を10とする
    def __init__(self, energy=10):
        self.energy = energy

    def eat_fruit(self):
        self.energy += 1
        return self

    def eat_meat(self):
        self.energy += 2
        return self

    def run(self):
        self.energy -= 3
        return self

#引数は不要(10なので)
anyone = Individual()
print("energy: {}".format(anyone.energy))
anyone.eat_meat()
print("energy after eat_meat: {}".format(anyone.energy))
anyone.eat_fruit()
print("energy after eat_fruit: {}".format(anyone.energy))
anyone.run()
print("energy after run: {}".format(anyone.energy))
anyone.eat_meat().run()
print("energy after eat_meat and run: {}".format(anyone.energy))