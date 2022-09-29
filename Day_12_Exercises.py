# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:40:47 2022

@author: ARMAN
"""

#%% LEVEL - 1
#1. Write a function which generates a six digit/character random_user_id.
def random_user_id():
    import random
    import string
    length = 5 #for 6 digits
    
    randomstr = ''.join(random.choices(string.ascii_letters + string.digits, k = length))
    
    return randomstr

print(random_user_id())
    
#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
#   One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    import random
    import string
    str_length = int(input('STRING LENGTH : '))
    run_length = int(input('HOW MUCH GEN : '))
    
    for i in range(run_length):
        randomstr = ''.join(random.choices(string.ascii_letters + string.digits, k = str_length))       
        print(randomstr)

user_id_gen_by_user()

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    import random
            
    list_for_rgb = list(range(0,256))
        
    random_r = random.choice(list_for_rgb)    
    random_g = random.choice(list_for_rgb)
    random_b = random.choice(list_for_rgb)
           
    return print("rgb({},{},{})".format(random_r, random_g, random_b))
    
rgb_color_gen()              

#%% LEVEL - 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
#   Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors():
    import random
    global randomhexa
        
    list_for_hexa_colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    randomhexa = ''
    
    for i in range(0,6):
        randomhexa += ''.join(random.choice(list_for_hexa_colors)) 
        
    randomhexa = '#' + randomhexa
    
    # print(randomhexa)
               
    return randomhexa

list_of_hexa_colors()

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors():
    import random
    global random_rgb
    list_for_rgb = list(range(0,256))
    random_r = random.choice(list_for_rgb)    
    random_g = random.choice(list_for_rgb)
    random_b = random.choice(list_for_rgb)
    
    random_rgb = 'rgb' + '(' + str(random_r) + ',' + str(random_g) + ',' + str(random_b) + ')'
    # print(random_rgb)
    
    return random_rgb

list_of_rgb_colors()

#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, count = 1):
    gen_color_arr = []
    if color_type == 'hexa':
        for i in range(count):        
            list_of_hexa_colors()
            gen_color_arr.append(randomhexa)
    
    if color_type == 'rgb': 
        for i in range(count): 
            list_of_rgb_colors()
            gen_color_arr.append(random_rgb)
            
    
    return print(gen_color_arr)

generate_colors('rgb',4)
#%% LEVEL - 3
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
def shuffle_list(liste):
    import random
    
    random.shuffle(liste)
    
    return print(liste)
    
shuffle_list([0,1,2,3,'a','b'])
#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def pick_elements():
    import random
    liste = list(range(10))
    random_pick_seven = random.sample(liste, 7)
    
    return print(random_pick_seven)

pick_elements()
