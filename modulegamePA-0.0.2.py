#-------------------------------------------------------------------------------
# Name:        modulegamePA
# Purpose:
#
# Author:      Jannis Kohlstrung
#
# Created:     01.01.2018
# Copyright:   (c) Jannis Kohlstrung + Paulo Fidalgo + tofutiger ( insert your name here if you want ) 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Version: 0.0.2
def main():
    pass

if __name__ == '__main__':
    main()

import random
import os

#Seriously time to start commenting this code.
player_name = input("What's your name?")
rand = ['mud']*6+['grass']*6+['wood']*3+['flowers']*3+['rock']*6+['rags','dagger','club'] #there should be a way of having different sets of rands for different world parts ( deserts, foests, etc )

characters_rand = ['Demon','Knight','Amazon','Ninja','Paladin','Barbarian','Fairy','Minotaur','Samurai','Onna-Bugeisha','Viking',"Arab Warrior",'Bear Man']

char_items = {'Demon':['demonic ski boots','demonic hair spray','demonic coin'], \
   'Guard':['long sword', 'sword', 'spear'],\
   'Amazon':['long sword', 'sword', 'battle axe', 'spear'],\
   'Knight':['long sword',], 'Paladin':['long sword'], 'Ninja':['dagger', 'spear', 'shuriken'], 'Barbarian':['battle axe','long axe'], \
   'Fairy':['dagger'], 'Minotaur':['dagger', 'long axe'], 'Shopkeeper':['dagger'], 'Blacksmith':['dagger'], 'Samurai':['Katana','Tashi','Dai-Katana'], \
   'Onna-Bugeisha':['Katana','Naginatta','Tashi'], 'Viking':['long sword', 'battle axe'], 'Bear Man':['Mace', 'spear'], 'Arab Warrior':['Scimitar','spear'], \
    }

my_damage=15
char_dict = {'Demon':{'name':'Demon','Foe':True,'Neutral':False,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':' ','weapon_equip':''}, \
  'Guard':{'name':'Guard','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             'Shopkeeper':{'name':'Shopkeeper','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Blacksmith':{'name':'Blacksmith','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Knight':{'name':'Knight','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Amazon':{'name':'Amazon','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Ninja':{'name':'Ninja','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Paladin':{'name':'Paladin','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Barbarian':{'name':'Barbarian','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Fairy':{'name':'Fairy','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
       'Samurai':{'name':'Samurai','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
       'Onna-Bugeisha':{'name':'Onna-Bugeisha','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Minotaur':{'name':'Minotaur','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Viking':{'name':'Viking','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Bear Man':{'name':'Bear Man','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
    'Arab Warrior':{'name':'Arab Warrior','Foe':False,'Neutral':True,'health':30,'strentght':10,'dexterity':10,'intelligence':10,'constitution':10,'charisma':10,'armor_equip':'full iron Armor','weapon_equip':''}, \
             }


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

my_world = \
  
  { (0,0): {'location':'town centre', 'descpt':'you are at the town center, it\'s beautiful, and there\'s a nice shop with some items for you, there is also a Blacksmith', 'items':['silver coin','dagger','wheel','sword'], 'characters':['Shopkeeper','Guard','Blacksmith']}, \
    (0,1): {'location':'the north', 'descpt':'you are at the North, it\'s very cold and there\'s an entrance to some caves', 'items':['coal','wood','flowers','moss'], 'characters':[]}, \
    (1,1): {'location':'the north-east', 'descpt':'you are at the north-east, there are many trees, you can see a river as well','items':['chips','wood'], 'characters':[]}, \
    (1,0): {'location':'the east', 'descpt':'you are at the East, it\'s mild and nice and you can see a river','items':['mud','wood','flowers','moss'], 'characters':[]}, \
    (0,-1): {'location':'the south', 'descpt':'you are at the south, it\'s very warm and you can see much white sand, there is a tent amazingly decorated', 'items':['dagger','moss'], 'characters':[]}, \
    (1,-1): {'location':'the south-east', 'descpt':'you are at the south-east, there\'s an huge forest of palmtrees and you can see the entrance for some dark caves', 'items':['wheat','wood','flowers','moss'], 'characters':[]}, \
    (-1,0): {'location':'the west', 'descpt':'you are at the west, it\'s beautiful and nice here, there is the entrance to a castle', 'items':['sword','dagger','flowers','moss'], 'characters':[]}, \
    (-1,-1): {'location':'the the South-west', 'descpt':'you are at the south-west, it\'s beautiful and nice here, there is the entrance to a zigurat made of stone', 'items':['sword','dagger','flowers','moss'], 'characters':[]}, \
    (-1,1): {'location':'the North-west', 'descpt':'you are at the NorthWest forest, it\'s very cold and beautiful and there is the entrance to a castle made of black stone', 'items':['sword','rock','rock','rock'], 'characters':[]}, \
    (-2,0): {'location':'the extreme West', 'descpt':'you are at the Extreme West forest, it\'s very mild and beautiful and you can see the ocean. There is a boat that will take you to the islands', 'items':['sword','rock','rock','rock'], 'characters':[]}, \
    (2,0): {'location':'the extreme East', 'descpt':'you are at the Extreme East, it\'s beautiful and nice here, there is the entrance to a sumptuous Palace', 'items':['gold coin','silver coin','flowers','dagger'], 'characters':['Ninja','Shopkeeper','Guard']}, \
    (0,2): {'location':'the North Pole', 'descpt':'you are at the glaciars of the North Pole, it\'s beautiful and epically cold here. You can see ice and Snow everywhere and it\'s snowing', 'items':['ice cube','arpoon','water','ice cube'], 'characters':['Bear Man','Viking']}, \
    (0,-2): {'location':'The Depths of the Desert', 'descpt':'you are at the Depths of the Southern Desert, all you can see is sand everywhere and the sun is very hot', 'items':['rock','sand'], 'characters':['Arab Warrior','Guard']} \
    }

 #start of the redoing of the whole thing into classes
 class Location:
   def __init__(self, name, description, items, characters):
       self.name = name
       self.description = description
       self.items = items
       self.characters=characters

locations = {
    (0, 0): Location(
        "Town Centre", "you are at the town center, it\'s beautiful, and there\'s a nice shop with some items for you, there is also a Blacksmith", ["silver coin", "dagger", "wheel", "sword"], ["Shopkeeper", "Guard", "Blacksmith"]
    )
}

#end of that
 
def see_place(my_world, my_x, my_y): 
    print(my_world[(my_x, my_y)]['descpt'])

def go_to(loc_x, loc_y):
    name = my_world[(loc_x, loc_y)][0]
    thing = my_world[(loc_x, loc_y)][1]
    return name, thing

def pickup(inventory,environment,item_num):
    inventory.append(environment[item_num])
    environment.remove(environment[item_num])
    environment.append(random.choice(rand))

def randoschar(characters_environ,characters_rand,char_dict,char_items):
    rand = char_dict[random.choice(characters_rand)]
    rand.update({'weapon_equip':random.choice(char_items[rand['name']])})
    return rand

def fight(characters_environ,stats,char_dict,obj_dict,inventory,character_number,player_hea):
    enemy_dead = 0;
    char = characters_environ[character_number]
    print('Enemy health: ' , char['health'], 'Your health: ' , player_hea)
    while char['health']>0 and player_hea > 0:
        dice=random.randint(0,1)
        if dice == 1:
            input_num = input('Strike with '+(', ').join([str(inventory.index(i)+1)+' '+i for i in inventory if obj_dict[i]['can_equip'] == True]))
            input_num = int(input_num)-1
            weapon = inventory[input_num]
            damage = random.randint(obj_dict[weapon]['min_damage'], obj_dict[weapon]['max_damage'])
            print ('you\'ve striken ',char['name'], 'with',weapon, 'and dealt', damage , 'points of damage')
            char['health'] = char['health'] - damage
            print('Enemy health: ' , char['health'], 'Your health: ' , player_hea)
        elif dice == 0:
            enemy_weapon = char['weapon_equip']
            enemy_damage = random.randint(obj_dict[enemy_weapon]['min_damage'], obj_dict[enemy_weapon]['max_damage'])
            print (char['name'], 'has stricken you with ', enemy_weapon, 'and dealt', enemy_damage, 'points of damage')
            player_hea = player_hea - enemy_damage
            print('Enemy health: ' , char['health'], 'Your health: ' , player_hea)
    else:
           if char['health'] <= 0:
               print (char['name'], ' is DEAD')
               enemy_dead = 1
               return enemy_dead
           elif player_hea <= 0:
               print ('you\'re DEAD')
               #exit()


def choose_class():
    game_class = input("What's your Class? (K)night, (B)arbarian, (V)iking, (P)aladin, (S)amurai, (O)nna-Bugeisha, (N)inja (R)ogue (T)hief Sor(C)erer").upper()
    valid_options = ['K', 'B', 'V', 'P', 'S', 'O', 'N', 'R', 'T', 'C']
    while game_class not in valid_options:
        print("You are only allowed to use one of the following options %s" % valid_options)
        game_class = input("What's your Class? (K)night, (B)arbarian, (V)iking, (P)aladin, (S)amurai, (O)nna-Bugeisha, (N)inja (R)ogue (T)hief Sor(C)erer").upper()

    return game_class

# Functions return anything; From an integer, to string to list. If return isn't used, it returns something called None.
# None is a special keyword in Python that means an "empty value".

# Here, we define another function that can receive an argument, called chosen_class. Each time we call this function, we must give it an argument, either as a static value or variable.
# For example confirm_class("K")
def confirm_class(chosen_class):
    if chosen_class == 'K':
        decision = input("You have chosen Knight, Knights are the most Ballanced Class, they are strong and not too slow, is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 12
           player_dex = 8
           player_int = 8
           player_hea = 10
           print("That's okay, you are a Knight, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'B':
        decision = input("you have Chosen Barbarian, Barbarians are very strong but also slow and dumb, is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 16
           player_dex = 6
           player_int = 5
           player_hea = 14
           print("That's okay, you are a Barbarian, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'V':
        decision = input("you have Chosen Viking, They are almost as strong as Barbarians but less slow and dumb, they also have a connection with the Runic realm. Is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 15
           player_dex = 7
           player_int = 7
           player_hea = 13
           print("That's okay, you are a Viking, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'P':
        decision = input("you have Chosen Paladin, they are somehow ballanced but highly intelligent and spiritual, is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 10
           player_dex = 9
           player_int = 11
           player_hea = 11
           print("That's okay, you are a Paladin, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'S':
        decision = input("you have Chosen Samurai, they are somehow ballanced but highly dexterous and lethal, is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 11
           player_dex = 12
           player_int = 9
           player_hea = 9
           print("That's okay, you are a Samurai, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
          return None
    elif chosen_class == 'O':
        decision = input("you have Chosen Onna-Bugeisha, they are somehow ballanced but highly dexterous and lethal, they are the female version of the Samurai, but they are more intelligent and Spiritual than them. Is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 10
           player_dex = 13
           player_int = 10
           player_hea = 10
           print("That's okay, you are an Onna-Bugeisha, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'N':
        decision = input("you have Chosen Ninja, they are somehow weak in strenght but are highly agile and lethal, as well as profoundly intelligent and Spiritual. Is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 6
           player_dex = 15
           player_int = 13
           player_hea = 8
           print("That's okay, you are a Ninja, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'R':
        decision = input("you have Chosen Rogue, they are somehow weak in strenght but are highly agile and dexterous, as well as profoundly intelligent and Masters on the art of Stealth and Long Range Attacks. They are like the Ninjas of the West. Is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 6
           player_dex = 15
           player_int = 12
           player_hea = 8
           print("That's okay, you are a Rogue, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'T':
        decision = input("you have Chosen Thief, they are very weak in strenght but are highly agile and dexterous, as well as profoundly intelligent and Masters on the art of Stealth and Deceaving. They are like Rogues but less efficient on long range attacks while being better at sneacking. Is this OKAY? (Y/N)")
        if decision == 'Y':
           player_str = 5
           player_dex = 15
           player_int = 13
           player_hea = 7
           print("That's okay, you are a Thief, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
    elif chosen_class == 'C':
        decision = input("you have Chosen Sorcerer. they are estremely weak in strenght but are epically intelligent and wise and Spiritual. They have a connection with the Gods and the realms of magick. Is this OKAY? (Y/N)").upper()
        if decision == 'Y':
           player_str = 5
           player_dex = 15
           player_int = 13
           player_hea = 7
           print("That's okay, you are a Sorcerer, your strenght is %s, your dexterity is %s, your intelligence is %s, and your health is %s" % (player_str, player_dex, player_int, player_hea))
           return player_str, player_dex, player_int, player_hea
        else:
           return None
# Here, we call the built-in Python function called input() that asks the user to type in a string.
# The return value is stored in a variable called name.
# Here, we store the return value from choose_class function in a variable called chosen_class.
chosen_class = choose_class()
stats = confirm_class(chosen_class)
while stats is None:
    chosen_class = choose_class()
    stats = confirm_class(chosen_class)

# This is a special trick in Pyther where you can unpack a list of values into many variables.
# For example: x, y, z = [1, 2, 3] will give 1, 2 and 3 values to x, y and z respectively.
# The below line works because confirm_class function returns a list when successful.
# It is important to keep the same logic for the rest of the classes (each 'Y' option should return a list of 3)
player_str, player_dex, player_int, player_hea2 = stats






my_x = 0
my_y = 0
inventory = []
newtile = 0;
enemy_status=0;



choose_class
confirm_class

print (chosen_class)
if chosen_class != 'S' and chosen_class != 'O' and chosen_class != 'P':
  chosen_genre=str(input("What is your Gender?").upper())
  if chosen_genre.startswith('F') and chosen_genre != 'F':
    chosen_genre = 'F'
    print('You are ' + chosen_genre)
  elif chosen_genre.startswith('M') and chosen_genre != 'M':
    chosen_genre = 'M'
    print('You are ' + chosen_genre)
  elif chosen_genre != 'M' and chosen_genre != 'F':
    print('You are only allowed to choose Male(M) or Female(F)')
    chosen_genre=str(input("What is your Gender?").upper())
  print('You are ' + chosen_genre)
elif chosen_class== 'S' or chosen_class == 'P':
  chosen_genre = 'M'
  print('You are ' + chosen_genre)
elif chosen_class == 'O':
  chosen_genre = 'F'
  print('You are ' + chosen_genre)

while True:
  environment = my_world[(my_x, my_y)]['items']
  characters_environ = [char_dict[char] for char in my_world[(my_x, my_y)]['characters']]
  for i in range(len(characters_environ)):
    char_toequip = characters_environ[i]
    characters_environ[i].update({'weapon_equip':random.choice(char_items[char_toequip['name']])})
  if newtile == 0 or enemy_status == 1:
   enemy = randoschar(characters_environ,characters_rand,char_dict,char_items)
   enemy_status = 0
  characters_environ.append(enemy)
  print("You are at " + my_world[(my_x, my_y)]['location'] + \
   " with " + (', ').join([str(environment.index(i)+1)+' '+i for i in environment])+ \
   " there's "+ (', ').join([str(characters_environ.index(i)+1)+' '+i['name'] for i in characters_environ]))
  mov = str(input('Enter direction (NSEW), (D)escription or (I)nventory: ').upper())

  try_x, try_y = my_x, my_y
  if mov == 'N':
    try_y += 1
  elif mov == 'S':
    try_y += -1
  elif mov == 'E':
    try_x += 1
  elif mov == 'W':
    try_x += -1
  elif mov == 'D':
    see_place(my_world, my_x, my_y)
  elif mov.startswith('G'):
    input_num = int(mov[1])-1
    pickup (inventory,environment,input_num)
  elif mov == 'I':
     for i in inventory:
      print(str(inventory.index(i)+1)+'\t'+i)
  elif mov.startswith('F'):
    character_number = int(mov[1])-1
    enemy_status = fight(characters_environ,stats,char_dict,obj_dict,inventory,character_number,player_hea2)


  else:
    print("Invalid move")

    continue
  if not (try_x, try_y) in my_world:
    print("Cannot move there")
  else:
    if my_x != try_x or my_y != try_y:
     my_x, my_y = try_x, try_y
     newtile = 0
    else:
     newtile = 1