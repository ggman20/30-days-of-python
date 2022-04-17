# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:04:46 2022

@author: ARMAN
"""

#%% LEVEL - 1
# 1. Create an empty tuple
empty_tuple = ()
empty_tuple2 = tuple()

# 2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters =  ('Mucize', 'Hanife', 'Şükran')
brothers = ('Hakan', 'Volkan', 'Yusuf', 'Osman')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
print('Total my siblings:', len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('İbrahim')
siblings.append('Hülya')
family_members = tuple(siblings)
print(family_members)

#%% LEVEL - 2 
# 1. Unpack siblings and parents from family_members
family_members = list(family_members)
parents = family_members[-2:]
siblings = family_members[0:(len(family_members) - 2)]
print(parents)
print(siblings)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('watermelon', 'apple', 'banana', 'orange')
vegetables = ('tomato', 'lettuce', 'pumpkin')
animal_products = ('lamb meat', 'milk', 'chicken meat', 'cheese', 'butter')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
import math
if(len(food_stuff_lt) == 1): 
    middle_item = food_stuff_lt[math.floor(len(food_stuff_lt)/2)]
    print('{} is the middle item of food_stuff'.format(middle_item))
else:    
    middle_item1 = food_stuff_lt[math.floor(len(food_stuff_lt)/2) - 1 ]
    middle_item2 = food_stuff_lt[math.floor(len(food_stuff_lt)/2)]
    print('{} and {} are middle items of food_stuff tuple and list'.format(middle_item1, middle_item2))

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-4:-1]
print('{} are first three items and {} are last three items of food stuff list'.format(first_three_items, last_three_items))

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    
# 7A.Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# 7B.Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)