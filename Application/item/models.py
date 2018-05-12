
char_items = {'Demon': ['demonic ski boots', 'demonic hair spray', 'demonic coin'], \
              'Guard': ['long sword', 'sword', 'spear'], \
              'Amazon': ['long sword', 'sword', 'battle axe', 'spear'], \
              'Knight': ['long sword', ], 'Paladin': ['long sword'], 'Ninja': ['dagger', 'spear', 'shuriken'],
              'Barbarian': ['battle axe', 'long axe'], \
              'Fairy': ['dagger'], 'Minotaur': ['dagger', 'long axe'], 'Shopkeeper': ['dagger'],
              'Blacksmith': ['dagger'], 'Samurai': ['Katana', 'Tashi', 'Dai-Katana'], \
              'Onna-Bugeisha': ['Katana', 'Naginatta', 'Tashi'], 'Viking': ['long sword', 'battle axe'],
              'Bear Man': ['Mace', 'spear'], 'Arab Warrior': ['Scimitar', 'spear'], \
              }


obj_dict = {
    'dagger': {'edible': False, 'can_equip': True, 'min_damage': 2, 'max_damage': 4, 'magic': False, 'block': 1}, \
    'sword': {'edible': False, 'can_equip': True, 'min_damage': 4, 'max_damage': 8, 'magic': False, 'block': 4}, \
    'long sword': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'spear': {'edibbe': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'battle axe': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'shuriken': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'Tashi': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'Katana': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'Dai-Katana': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'Naginatta': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'long axe': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'club': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'Mace': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    'Scimitar': {'edible': False, 'can_equip': True, 'min_damage': 6, 'max_damage': 11, 'magic': False, 'block': 6}, \
    }

class Item:

    def __init__(self, name = "Item"):
        self.name = name

    def __str__(self):
        return self.name


class Dagger(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 2
        self.max_damage = 4
        self.magic = False
        self.block = 1


class Sword(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 4
        self.max_damage = 8
        self.magic = False
        self.block = 4


class LongSword(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Spear(Item):

    def __init__(self):
        self.edibbe = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class BattleAxe(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Shuriken(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Tashi(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Katana(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class DaiKatana(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Naginatta(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class LongAxe(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Club(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Mace(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6


class Scimitar(Item):

    def __init__(self):
        self.edible = False
        self.can_equip = True
        self.min_damage = 6
        self.max_damage = 11
        self.magic = False
        self.block = 6
