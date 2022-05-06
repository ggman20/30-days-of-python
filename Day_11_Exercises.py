# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:12:23 2022

@author: ARMAN
"""

#%% LEVEL - 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(1, 5))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r, pi = 3.14):
    area = pi * (r ** 2)
    return area

print(area_of_circle(1))
# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types.
#    If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    
    for num in nums:
        if (type(num) == int or type(num) == float):
            total = total + num           
        else:
            total = None
            print('All parameters are not number types')
    return total

print(add_all_nums(5,6,7,'kek'))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(25))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if (month == 'December' or month == 'January' or month == 'February'):
        season = 'Winter'
    if (month == 'March' or month == 'April' or month == 'May'):
        season = 'Spring'
    if (month == 'June' or month == 'July' or month == 'August'):
        season = 'Summer'
    if (month == 'September' or month == 'October' or month == 'November'):
        season = 'Autumn'
    return season

print(check_season('April'))
        
# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,x2,y1,y2):
    m = (y2 - y1)/(x2 - x1)
    return m

print(calculate_slope(1, 2, 5, 6))
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    discriminant = (b * b) - (4 * a * c)
    if (discriminant == 0):
        print('discriminant = 0')
        x1 = (-1 * b) / (2 * a)
        x2 = x1
    elif (discriminant > 0):
        print('discriminant > 0')
        x1 = ((-1 * b) - (discriminant)) / (2 * a)
        x2 = ((-1 * b) + (discriminant)) / (2 * a)
    elif (discriminant < 0):
        print('discriminant < 0')
        x1 = str(((-1 * b) / (2 * a))) + '-' + (str((discriminant) / (2 * a)) + 'i')
        x2 = str(((-1 * b) / (2 * a))) + '+' + (str((discriminant) / (2 * a)) + 'i')
    return x1, x2

print("x1 and x2:", solve_quadratic_eqn(11, 1, 5))
        
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(liste):
    for item in liste:
        print(item)
        
print_list([1,2,3,'kek'])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
import math
def reverse_list(array):
    n = math.floor(len(array)/2)
    last_index = len(array) - 1
    for i in range(n):
        temp = array[i]
        array[i] = array[last_index - i]
        array[last_index - i] = temp
    return array

print(reverse_list([1,2,3,4,5,6, 'kek', 'sek']))
        
# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalized_list_items(liste):
    new_list = []
    for item in liste:
        new_item = item.capitalize()
        new_list.append(new_item)
        

    return new_list
print(capitalized_list_items(['lion', 'king', 'galatasaray', 'oooo']))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(liste, *items):
    for item in items:
        liste.append(item)
        
    return liste
print(add_item([1,2,3,4,5,'kek','sek'], 6,7,8,9,'exist', 'last'))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(liste, *items):
    for item in items:
        if (item in liste):
            liste.remove(item)
        else:
            continue
    return liste
print(remove_item([1,2,3,4,5,'kek','sek'], 1,5,'kek'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(liste, number):
    new_list = []
    
    for i in range(len(liste)):
        if(type(liste[i]) == int or type(liste[i]) == float):
            new_list.append(liste[i] + number)
        else:
            continue

    return new_list

print(sum_of_numbers([1,2,3,4,5,'kek','sek',6,7,8], 5))
# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(liste, number):
    new_list = []
    for i in range(len(liste)):
        if((type(liste[i]) == int or type(liste[i]) == float) and liste[i] % 2 == 1):           
            new_list.append(liste[i] + number)
        else:
            continue

    return new_list
print(sum_of_odds([1,2,3,4,5,'kek','sek',6,7,8], 5))
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(liste, number):
    new_list = []
    for i in range(len(liste)):
        if((type(liste[i]) == int or type(liste[i]) == float) and liste[i] % 2 == 0):           
            new_list.append(liste[i] + number)
        else:
            continue

    return new_list
print(sum_of_even([1,2,3,4,5,'kek','sek',6,7,8], 5))

#%% LEVEL - 2
# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(int_number):
    odds = 0
    evens = 0
    print('here1')
    if(type(int_number) == int):
        print('here2')
        for i in range(int_number + 1):
            if (i % 2 == 0):
                evens = evens + 1
            else:
                odds = odds + 1
           
    return evens, odds
print('evens and odds -->',evens_and_odds(100))

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    fac = 1
    for i in range(1, number + 1):
        fac = fac * i
    return fac
print('Factorial of {} is:'.format(5), factorial(5))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
a_list = [1,2,3,5,8,10,'no','yes']
def is_empty(item):
    cond = 0
    for i in range(len(a_list)):
        if (a_list[i] == item):
            cond = 1
            print('item is here')
       
is_empty(3)           

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, 
#    calculate_std (standard deviation).
def calculate_mean(liste):
    sum_list = 0
    for i in range(len(liste)):
        sum_list += i
    mean = sum_list / len(liste)
    return mean
print("mean:",calculate_mean([1,2,3,4,5,6,7,8]))

def calculate_median(liste):
    median = []
    if(len(liste) % 2 == 1):
        for i in range(len(liste)):
            median_odd = liste[math.floor(len(liste)/2)] 
        median.append(median_odd)
    elif(len(liste) % 2 == 0):
        for i in range(len(liste)):
            median_even1 = liste[math.floor(len(liste)/2)] 
            median_even2 = liste[math.floor((len(liste)/2)) - 1] 
        median.append(median_even1)
        median.append(median_even2)
    return median      
print("Median:",calculate_median([1,2,3,4,5,6,7,8]))
           
def calculate_mode(liste):
    frequency = {}
    
    for item in liste:
        frequency[item] = frequency.get(item, 0) + 1
        
    most_frequent = max(frequency.values())
    
    modes = [key for key, item in frequency.items() if item == most_frequent]
    
    return modes

print(calculate_mode([1,2,3,4,5,6,7,8,3,3,5,5,5,5,2,8,4,5]))

def calculate_range(liste):
    liste.sort()
    minimum_value = liste[0]
    maximum_value = liste[len(liste) - 1]
    return minimum_value, maximum_value

print('the range is:',calculate_range([1,2,3,4,5,6,7,8,3,3,5,5,5,5,2,8,4,5,9]))
    
def calculate_variance(liste):
    sum_liste = 0
    for i in range(len(liste)):
        sum_liste = sum_liste + liste[i]
    average_liste = sum_liste / len(liste)
    temp_value = 0
    for i in range(len(liste)):
        temp_value += ((liste[i] - average_liste) ** 2)
    variance = temp_value / len(liste)
    return variance
print(calculate_variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
import math
def calculate_std(liste):
    variance = calculate_variance(liste)
    std = math.sqrt(variance)
    return std

print(calculate_std([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))

#%% LEVEL - 3
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    count = 0
    
    for i in range(1,number):
        if number % i != 0:
            count = count + 1
    print(count)     
    if count == (number - 2):
        print('{} is a prime number '.format(number))
    else:
        print('{} is not a prime number'.format(number))

is_prime(32)        
# 2. Write a functions which checks if all items are unique in the list.
def is_unique(liste):
    
        
        
    

# 3. Write a function which checks if all the items of the list are of the same data type.
def is_same_data_type(liste):
    


# 4. Write a function which check if provided variable is a valid python variable



# 5. Go to the data folder and access the countries-data.py file.


# 5A. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order


# 5B. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.











