# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 08:51:38 2022

@author: ARMAN
Lesson : List Comprehension
"""

#%% NO LEVEL
#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

not_positive_numbers = [number for number in numbers if number <= 0]
print(not_positive_numbers)

#2. Flatten the following list of lists of lists to a one dimensional list 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [j for i in list_of_lists for k in i for j in k]
print(flattened_list)
    
#3. Using list comprehension create the following list of tuples
list_of_tuples = [(i,1,i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_of_tuples)

#4. Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flatten_countries = [[k[0].upper(), k[0][0:3].upper(), k[1].upper()] for i in countries for k in i]  
print(flatten_countries)
  
#5. Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_countries = [{'country': k[0].upper(), 'city': k[1].upper()} for row in countries for k in row]
print(dict_countries)

#6. Change the following list of lists to a list of concatenated strings
names = [[('Gokhan', 'Arman')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concatenated_strings = [k[0] +' '+ k[1]  for row in names for k in row]
#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)

slope(4,5,8,10)
