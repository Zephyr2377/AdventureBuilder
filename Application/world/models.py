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

my_world = {(0, 0): {'location': 'town centre',
                     'descpt': 'you are at the town center, it\'s beautiful, and there\'s a nice shop with some items for you, there is also a Blacksmith',
                     'items': ['silver coin', 'dagger', 'wheel', 'sword'],
                     'characters': ['Shopkeeper', 'Guard', 'Blacksmith']}, \
            (0, 1): {'location': 'the north',
                     'descpt': 'you are at the North, it\'s very cold and there\'s an entrance to some caves',
                     'items': ['coal', 'wood', 'flowers', 'moss'], 'characters': []}, \
            (1, 1): {'location': 'the north-east',
                     'descpt': 'you are at the north-east, there are many trees, you can see a river as well',
                     'items': ['chips', 'wood'], 'characters': []}, \
            (1, 0): {'location': 'the east',
                     'descpt': 'you are at the East, it\'s mild and nice and you can see a river',
                     'items': ['mud', 'wood', 'flowers', 'moss'], 'characters': []}, \
            (0, -1): {'location': 'the south',
                      'descpt': 'you are at the south, it\'s very warm and you can see much white sand, there is a tent amazingly decorated',
                      'items': ['dagger', 'moss'], 'characters': []}, \
            (1, -1): {'location': 'the south-east',
                      'descpt': 'you are at the south-east, there\'s an huge forest of palmtrees and you can see the entrance for some dark caves',
                      'items': ['wheat', 'wood', 'flowers', 'moss'], 'characters': []}, \
            (-1, 0): {'location': 'the west',
                      'descpt': 'you are at the west, it\'s beautiful and nice here, there is the entrance to a castle',
                      'items': ['sword', 'dagger', 'flowers', 'moss'], 'characters': []}, \
            (-1, -1): {'location': 'the the South-west',
                       'descpt': 'you are at the south-west, it\'s beautiful and nice here, there is the entrance to a zigurat made of stone',
                       'items': ['sword', 'dagger', 'flowers', 'moss'], 'characters': []}, \
            (-1, 1): {'location': 'the North-west',
                      'descpt': 'you are at the NorthWest forest, it\'s very cold and beautiful and there is the entrance to a castle made of black stone',
                      'items': ['sword', 'rock', 'rock', 'rock'], 'characters': []}, \
            (-2, 0): {'location': 'the extreme West',
                      'descpt': 'you are at the Extreme West forest, it\'s very mild and beautiful and you can see the ocean. There is a boat that will take you to the islands',
                      'items': ['sword', 'rock', 'rock', 'rock'], 'characters': []}, \
            (2, 0): {'location': 'the extreme East',
                     'descpt': 'you are at the Extreme East, it\'s beautiful and nice here, there is the entrance to a sumptuous Palace',
                     'items': ['gold coin', 'silver coin', 'flowers', 'dagger'],
                     'characters': ['Ninja', 'Shopkeeper', 'Guard']}, \
            (0, 2): {'location': 'the North Pole',
                     'descpt': 'you are at the glaciars of the North Pole, it\'s beautiful and epically cold here. You can see ice and Snow everywhere and it\'s snowing',
                     'items': ['ice cube', 'arpoon', 'water', 'ice cube'], 'characters': ['Bear Man', 'Viking']}, \
            (0, -2): {'location': 'The Depths of the Desert',
                      'descpt': 'you are at the Depths of the Southern Desert, all you can see is sand everywhere and the sun is very hot',
                      'items': ['rock', 'sand'], 'characters': ['Arab Warrior', 'Guard']} \
            }

