class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:
    def __init__(self):
        self.units = []
        self._alives = 0

    @property
    def alives(self):
        return self._alives

    @alives.setter
    def alives(self, param):
        self._alives = param

    def add_units(self, unit_type, number):
        for i in range(number):
            self.units.append(unit_type())
        self._alives += number

    def take_fighter(self):
        return self.units[len(self.units) - self.alives] \
            if self.alives else None


class Battle:
    def fight(self, army_1, army_2):
        unit_1 = army_1.take_fighter()
        unit_2 = army_2.take_fighter()
        while army_1.alives and army_2.alives:
            if fight(unit_1, unit_2):
                army_2.alives -= 1
                unit_2 = army_2.take_fighter()
            else:
                army_1.alives -= 1
                unit_1 = army_1.take_fighter()
        return army_1.alives > 0


def fight(unit_1, unit_2):
    while unit_1.is_alive:  # and unit_2.is_alive
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            return True
        unit_1.health -= unit_2.attack
    return False  # unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")