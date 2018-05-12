characters_rand = ['Demon', 'Knight', 'Amazon', 'Ninja', 'Paladin', 'Barbarian', 'Fairy', 'Minotaur', 'Samurai', 'Onna-Bugeisha', 'Viking', "Arab Warrior", 'Bear Man']

char_dict = {'Demon':{'name':'Demon','Foe':True,'Neutral':False,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':' ','weapon_equip':''}, \
             'Guard':{'name':'Guard','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Shopkeeper':{'name':'Shopkeeper','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Blacksmith':{'name':'Blacksmith','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Knight':{'name':'Knight','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Amazon':{'name':'Amazon','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Ninja':{'name':'Ninja','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Paladin':{'name':'Paladin','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Barbarian':{'name':'Barbarian','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Fairy':{'name':'Fairy','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Samurai':{'name':'Samurai','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Onna-Bugeisha':{'name':'Onna-Bugeisha','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Minotaur':{'name':'Minotaur','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Viking':{'name':'Viking','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Bear Man':{'name':'Bear Man','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Arab Warrior':{'name':'Arab Warrior','Foe':False,'Neutral':True,'health':30,'strength':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             }


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


# dict_to_class(char_dict, 'Character')

# for items in char_items:
#     for item in char_items[items]:


class Character:

    def __init__(self, name = "Character"):
        self.name = name

    def __str__(self):
        return self.name


class Demon(Character):

    def __init__(self):
        self.name = Demon
        self.Foe = True
        self.Neutral = False
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = None
        self.weapon_equip = None


class Guard(Character):

    def __init__(self):
        self.name = Guard
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = "full iron Armor"
        self.weapon_equip = None


class Shopkeeper(Character):

    def __init__(self):
        self.name = Shopkeeper
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Blacksmith(Character):

    def __init__(self):
        self.name = Blacksmith
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'ull iron Armor'
        self.weapon_equip = None


class Knight(Character):

    def __init__(self):
        self.name = Knight
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Amazon(Character):

    def __init__(self):
        self.name = Amazon
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Ninja(Character):

    def __init__(self):
        self.name = Ninja
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Paladin(Character):

    def __init__(self):
        self.name = Paladin
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Barbarian(Character):

    def __init__(self):
        self.name = Barbarian
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Fairy(Character):

    def __init__(self):
        self.name = Fairy
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Samurai(Character):

    def __init__(self):
        self.name = Samurai
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class OnnaBugeisha(Character):

    def __init__(self):
        self.name = 'Onna-Bugeisha'
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Minotaur(Character):

    def __init__(self):
        self.name = Minotaur
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class Viking(Character):

    def __init__(self):
        self.name = 'Viking'
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class BearMan(Character):

    def __init__(self):
        self.name = 'Bear Man'
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


class ArabWarrior(Character):

    def __init__(self):
        self.name = 'Arab Warrior'
        self.Foe = False
        self.Neutral = True
        self.health = 30
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.constitution = 10
        self.charisma = 10
        self.armor_equip = 'full iron Armor'
        self.weapon_equip = None


john = ArabWarrior()

print(john.name)
print(john)