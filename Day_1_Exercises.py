# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:11:14 2022

@author: ARMAN
"""
#%% LEVEL-1
# 1. Check the python version you are using
import sys
print("Python Version", sys.version_info)

# 2. Open the python interactive shell and do the following operations. 
#    The operands are 3 and 4
#    addition(+), subtraction(-), multiplication(*), modulus(%),division(/),exponential(**) 
#    floor division operator(//)   
print("addition(+)", 3 + 4)
print("subtraction(-)", 3 - 4)
print("multiplication(*)", 3 * 4)
print("modulus(%)", 3 % 4)
print("division(/)", 3 / 4)
print("exponential(**)", 3 ** 4)
print("floor division operator(//)", 3 // 4)

# 3. Write strings on the python interactive shell. The strings are the following   
# Your name, Your family name, Your country, I am enjoying 30 days of python
print('My name:', 'Gökhan')
print('My family name:', 'Arman')
print('My country:', 'Turkey')
print('I am enjoying 30 days of python')

# 4. Check the data types of the following data
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Gökhan', 'Python', 'Turkey']))
print(type('Gökhan'))
print(type('Arman'))
print(type('Turkey'))

#%% LEVEL-2

# Create a folder named day_1 inside 30DaysOfPython folder.
# Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. 
# Remember to use print() when you are working on a python file. 
# Navigate to the directory where you have saved your file, and run it.
print('DONE')

#%%  LEVEL-3
# Write an example for different Python data types such as Number
# (Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print(10)
print(3.8)
print(5 - 6j)
print('Gökhan')
print(True)
print(['Thrones', 12, 'wHAt'])  #List
print(('Ne', 'What', 'Kral', 'King'))  # Tuple
print({'Good', 'Evening', 'My', 'Lord'}) # Set
print({'Name': 'Gökhan', 'Surname': 'Arman', 'Country' : 'Turkey', 'Age': 33})  #Dictionary

# Find an Euclidian distance between (2, 3) and (10, 8)
euclidianDistance = (((2 - 3) ** 2)) + ((10 - 8) ** 2)
print(euclidianDistance)





