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
languages_all_array = []
lang_str = ""
for i in range(len(data_of_countries)):
    lang_arr = data_of_countries[i]['languages']
    languages_all_array.append(lang_arr)
      
print(languages_all_array) 

for k in range(len(languages_all_array)):    
    for j in range(len(languages_all_array[k])):
        if (lang_str.__contains__(languages_all_array[k][j]) == False):
            # listToStr = ' '.join(map(str, languages_all_array[k]))
            lang_str += languages_all_array[k][j] + ','
            
print("lang_str",lang_str)
lang_arr = list(lang_str.split(','))
print(lang_arr)
new_lang_arr = []
for i in range(len(lang_arr)):
    if(lang_arr[i].__contains__('modern') == False):
        new_lang_arr.append(lang_arr[i])
new_lang_arr.pop()   
print("new_lang", new_lang_arr)
print("The total number of languages:", len(new_lang_arr))

# 3B.Find the ten most spoken languages from the data
all_langs_str = ""
for k in range(len(languages_all_array)):    
    for j in range(len(languages_all_array[k])):
        all_langs_str += languages_all_array[k][j] + ','
print(all_langs_str)

counted_arr = []
for i in range(len(new_lang_arr)):
    counted = all_langs_str.count(new_lang_arr[i])
    counted_arr.append(counted)
    
print(counted_arr)
most_spoken_langs = []
for i in range(len(counted_arr)):
    if(counted_arr[i] > 4):
       most_spoken_langs.append(new_lang_arr[i])
       
print("Ten most spoken languages:",most_spoken_langs)

# 3C.Find the 10 most populated countries in the world
population_arr = []
name_arr = []
for i in range(len(data_of_countries)):   
    population_arr.append(data_of_countries[i]["population"])
    name_arr.append(data_of_countries[i]["name"])
print(name_arr)
print(population_arr)
final_list = []
most_pop_country_list = []
for i in range(10): 
    max1 = 0   
          
    for j in range(len(population_arr)):     
        if population_arr[j] > max1:
            max1 = population_arr[j];
            index = j
            
    population_arr.remove(max1);
    final_list.append(max1)
    most_pop_country_list.append(data_of_countries[index]['name'])
          
print(final_list) #[1377422166, 1295210000, 323947000, 258705000, 206135893, 194125062, 186988000, 161006790, 146599183, 126960000]
print(most_pop_country_list) #['China', 'Iceland', 'United Arab Emirates', 'Iceland', 'Brazil', "Korea (Democratic People's Republic of)", 'New Caledonia', 'Bangladesh', 'Poland', 'Ireland']

    


