# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:50:22 2022

@author: ARMAN
Lesson : High Order Functions
"""


#%% 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#%% LEVEL - 1
# 1. Explain the difference between map, filter, and reduce.

# The map() function returns a new array through passing a function over each element in the input array. 
# This is different to reduce() which takes an array and a function in the same way, but the function takes 2 inputs - an accumulator and a current value.
# So reduce() could be used like map() if you always .concat onto the accumulator the next output from a function

# 2. Explain the difference between higher order function, closure and decorator

# A higher order function is a function that takes a function as an argument OR* returns a function.
# A decorator in Python is (typically) an example of a higher-order function, but there are decorators that aren't 
# (class decorators**, and decorators that aren't functions), and there are higher-order functions that aren't decorators. 
# for example those that take two required arguments that are functions.

# 3. Define a call function before map, filter or reduce, see examples.
def call_function(x):
    return x ** 2

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)

#%% LEVEL - 2
# 1. Use map to create a new list by changing each country to uppercase in the countries list
# Old method
country_upper = []
for country in countries:
    country_upper.append(country.upper())
    
print('Upper',country_upper)

# List comprehension
country_upper2 = [country.upper() for country in countries]
print('Upper2', country_upper2)

# map() method
def upper(x):
    return x.upper()

country_upper3 = map(upper, countries)
country_upper3 = list(country_upper3)
print('Upper3', country_upper3)

# 2. Use map to create a new list by changing each number to its square in the numbers list
# Old method
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print('Squared', squared_numbers)    

# List comprehension
squared_numbers2 = [number ** 2 for number in numbers]
print('Squared2', squared_numbers2)

# map() method
def square(x):
    return x ** 2

squared_numbers3 = list(map(square, numbers))
print('Squared3', squared_numbers3)

# 3. Use map to change each name to uppercase in the names list
# Old method
name_upper = []
for name in names:
    name_upper.append(name.upper())
    
print('Upper', name_upper)

# List comprehension
upper_name2 = [name.upper() for name in names]
print('Upper2', upper_name2)

# map() method
# upper was definied
upper_name3 = list(map(upper, names))
print('Upper3', upper_name3)

# 4. Use filter to filter out countries containing 'land'.
# Old method
with_land = []
for country in countries:
    if country.__contains__('land')== True:
        with_land.append(country)

print('land',with_land)

# List comprehension
with_land2 = [country for country in countries if country.__contains__('land')]
print('land2',with_land2)

# filter() method
def land(x):
    if x.__contains__('land'):
        return True
    return False

with_land3 = list(filter(land, countries))
print('Land3',with_land3)
# 5. Use filter to filter out countries having exactly six characters.
# Old method
six_char = []
for country in countries:
    if len(country) == 6:
        six_char.append(country)

print('Six', six_char)

# List comprehensions
six_char2 = [country for country in countries if len(country) == 6]
print('Six2', six_char2)

# filter() method
def six_char_func(x):
    if len(x) == 6:
        return True
    return False

six_char3 = list(filter(six_char_func, countries))
print('Six3', six_char3)
# 6. Use filter to filter out countries containing six letters and more in the country list.
def more_than_five(x):
    if len(x) > 5:
        return True
    return False

more_five_char = list(filter(more_than_five, countries))
print(more_five_char)

# 7. Use filter to filter out countries starting with an 'E'
def start_with_E(x):
    if x.startswith('E'):
        return True
    return False

starts_with_E = list(filter(start_with_E, countries))
print(starts_with_E)
# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Old method
empty_list = []
def get_string_lists(liste):
    for item in liste:
        if type(item) == str:
            empty_list.append(item)
            
    return empty_list
get_string_lists(['a',1,'b'])

# filter() method
liste2 = ['a', 5, 'gg', 7,'kek']
def it_is_str(x):
    if type(x) == str:
        return True
    return False
string_items = list(filter(it_is_str, liste2))
print(string_items)
            
# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
def sum_func(x1, x2):
    return x1 + x2
sum_numbers = reduce(sum_func, numbers)
print(sum_numbers)
# 11. Use reduce to concatenate all the countries and to produce this sentence: 
#     Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def sentence(country1, country2):
    return ''.join(country1 +', ' + country2)
                 
kek = reduce(sentence, countries)
print('{} are north European countries'.format(kek))

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern 
#     (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countriesall import countriesall
def land_countries(country):
    if country.__contains__('land'):
        return True
    return False

def ia_countries(country):
    if country.__contains__('ia'):
        return True
    return False

def island_countries(country):
    if country.__contains__('island'):
        return True
    return False

def stan_countries(country):
    if country.__contains__('stan'):
        return True
    return False
with_land_all = list(filter(land_countries, countriesall))
with_ia_all = list(filter(ia_countries, countriesall))
with_island_all = list(filter(island_countries, countriesall))
with_stan_all = list(filter(stan_countries, countriesall))
print('land', with_land_all)
print('ia', with_ia_all)
print('island', with_island_all)
print('stan',with_stan_all)

# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names
#     starting with that letter.
#countries_dicts = [{'country': xxx, 'rep': XXX, 'number': 1}]
countries_dicts = [{'country': country.upper(), 'rep': country[0:3].upper(), 'number': countriesall.index(country) + 1 } for country in countriesall]
print(countries_dicts)

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(liste):
    first_ten_countries = [country for country in liste if liste.index(country) < 10 ]
    return first_ten_countries
print(get_first_ten_countries(countriesall))           

# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(liste):
    last_ten_countries = [country for country in liste if liste.index(country) > len(liste) - 11 ]
    return last_ten_countries
print(get_last_ten_countries(countriesall))   
    
#%% LEVEL - 3
# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    Sort countries by name, by capital, by population
#    Sort out the ten most spoken languages by location.
#    Sort out the ten most populated countries.

from countries_data import data

by_name = data.copy()
by_name.sort(key = lambda x:x['name'])
print('NAME',by_name)

by_capital = data.copy()
by_capital.sort(key = lambda x:x['capital'])
print('CAPITAL',by_capital)

by_population = data.copy()
by_population.sort(key = lambda x:x['population'])
print('POPULATION',by_population)

most_ten_spoken = data.copy()
most_ten_spoken.sort(key = lambda x:x['population'].lower())








