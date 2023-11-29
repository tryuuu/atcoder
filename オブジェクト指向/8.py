#7.pyの書き換え
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

class Boy(Individual):
    def __init__(self, energy=10):
        super().__init__(energy)

    def daily_activity(self):
        self.eat_meat().eat_meat().run().eat_meat().eat_fruit().run().eat_meat()
        print("boy's daily energy: {}".format(self.energy))


class Girl(Individual):
    def __init__(self, energy=10):
        super().__init__(energy)

    def daily_activity(self):
        self.eat_meat().eat_fruit()
        print("girl's daily energy: {}".format(self.energy))

bob = Boy()
bob.daily_activity()
mary = Girl()
mary.daily_activity()