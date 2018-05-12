characters_rand = ['Demon', 'Knight', 'Amazon', 'Ninja', 'Paladin', 'Barbarian', 'Fairy', 'Minotaur', 'Samurai', 'Onna-Bugeisha', 'Viking', "Arab Warrior", 'Bear Man']


class Character:

    def __init__(self, name=None):
        self.name = name
        print("your char name is " + self.name)


class Demon(Character):
    pass