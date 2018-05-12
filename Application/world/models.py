def dict_to_class(dictionary, class_extend): # works only for 2 deep dictionary
    for character in dictionary: # Main outside dictionary
        print('\n')
        new_item = ''
        new_character = character.title()
        for letter in new_character:
            if not letter.isspace():
                new_item += letter
        print('class {}({}): \n'.format(new_item, class_extend )) # create main class
        print('\tdef __init__(self):') # create constructor
        for item in dictionary[character]:
            # if isinstance(item, str):
            # item = "\'"+item+"\'"
            print('\t\tself.{} = {}'.format(item, dictionary[character][item])) # add items.

obj_dict = {'dagger':{'edible':False,'can_equip':True,'min_damage':2,'max_damage':4,'magic':False,'block':1}, \
            'sword':{'edible':False,'can_equip':True,'min_damage':4,'max_damage':8,'magic':False,'block':4}, \
            'long sword':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'spear':{'edibbe':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'battle axe':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'shuriken':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'Tashi':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'Katana':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'Dai-Katana':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'Naginatta':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'long axe':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'club':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'Mace':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
            'Scimitar':{'edible':False,'can_equip':True,'min_damage':6,'max_damage':11,'magic':False,'block':6}, \
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
