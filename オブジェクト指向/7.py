#オブジェクトの動的操作
class Individual:
    #初期値を10とする、initにしないとコンストラクタにならない
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
#クラスの継承、Individualを二度も書く必要がない
class Boy(Individual):
    def daily_activity(self):
        self.eat_meat().eat_meat().run().eat_meat().eat_fruit().run().eat_meat()
        print("boy's daily energy: {}".format(self.energy))


class Girl(Individual):
    def daily_activity(self):
        self.eat_meat().eat_fruit()
        print("girl's daily energy: {}".format(self.energy))


bob = Boy()
bob.daily_activity()
mary = Girl()
mary.daily_activity()