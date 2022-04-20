# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:35:36 2022

@author: ARMAN
"""
#%% LEVEL - 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
i = 0
while i < 11:   
    print(i)
    i = i + 1
    
# 2. Iterate 10 to 0 using for loop, do the same using while loop.
i = 11
for i in range(11):   
    print(i)
    i = i - 1
    
# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# diyez = ['#']
# for i in range(7):
#     diyez.append('#')
#     listToStr = ' '.join(map(str, diyez))
#     print(listToStr) 
   
# 4. Use nested loops to create the following:
diyez = ['#']
listToStr = ''
for i in range(8):
    diyez.append('#')
    listToStr = ' '.join(map(str, diyez))
for j in range(8):
    print(listToStr)
    
# 5. Print the following pattern:
for i in range(11):
    result = i * i
    print('{} x {} = {}'.format(i, i, result))
    
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lang_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in lang_list:
    print(lang)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 100, 2):
    print(i)

#%% LEVEL - 2 
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_number = 0
for i in range(101):
    sum_number = sum_number + i
print('sum of 0 to 100 all numbers:', sum_number)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0
for i in range(0,101,2):
    sum_evens = sum_evens + i
for k in range(1,100,2):
    sum_odds =sum_odds + k
print('sum of 0 to 100 all even numbers:', sum_evens)
print('sum of 0 to 100 all odd numbers:', sum_odds)

#%% LEVEL - 3

# 1. Go to the data folder and use the countries.py file. 
#    Loop through the countries and extract all the countries containing the word land.
import countries
countries_array = countries.countries
countries_with_land = []
for country in countries_array:
    if(country.__contains__('land')):
        countries_with_land.append(country)
print(countries_with_land)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
import math
n = math.floor(len(fruits)/2)
last_index = len(fruits) - 1
for i in range(n):
    temp = fruits[i]
    fruits[i] = fruits[last_index - i]
    fruits[last_index - i] = temp
print(fruits) 
    
# 3. Go to the data folder and use the countries_data.py file.
import countries_data
data_of_countries = countries_data.data
print(data_of_countries)
# 3A.What are the total number of languages in the data
for i in range(len(data_of_countries)):
    print(data_of_countries[i]['languages'])



# 3B.Find the ten most spoken languages from the data

# 3C.Find the 10 most populated countries in the world


