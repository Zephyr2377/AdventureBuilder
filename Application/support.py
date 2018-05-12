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