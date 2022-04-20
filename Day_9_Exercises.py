# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:37:29 2022

@author: ARMAN
"""

#%% LEVEL - 1
# 1. Get user input using input(“Enter your age: ”). 
#    If user is 18 or older, give feedback: You are old enough to drive. 
#    If below 18 give feedback to wait for the missing amount of years.
your_age = int(input('What is your age?:'))

if (your_age >= 18):
    print('You are old enough to drive.')
else:
    print('You are young to drive.Wait for the missing amount of years.')

# 2. Compare the values of my_age and your_age using if … else. 
#    Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#    You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger 
#    differences, and a custom text if my_age = your_age.
my_age = 33
difference_age = abs(my_age - your_age)
if(my_age > your_age):    
    if (difference_age == 1):
        print('I am only one year older than you.')
    else:
        print('I am {} years older than you'.format(difference_age))
elif(your_age > my_age):
    if (difference_age == 1):
        print('You are only one year older than me.')
    else:
        print('You are {} years older than me'.format(difference_age))
elif(your_age == my_age):
    print('Your age and my age is equal')

# 3. Get two numbers from the user using input prompt. 
#    If a is greater than b return a is greater than b, if a is less b return a is smaller than b,
#    else a is equal to b.
a = int(input('a:'))
b = int(input('b:'))
if(a > b):
    print('a is greater than b')
elif(b > a):
    print('b is greater than a')
elif(a == b):
    print('a is equal to b.')

#%% LEVEL - 2
# 1. Write a code which gives grade to students according to theirs scores:
exam_score = int(input('Exam Score:'))
if(exam_score >= 80 and exam_score <= 100):
    print('A')
elif(exam_score >= 70 and exam_score <= 89):
    print('B')
elif(exam_score >= 60 and exam_score <= 69):
    print('C')
elif(exam_score >= 50 and exam_score <= 59):
    print('D')
elif(exam_score >= 0 and exam_score <= 49):
    print('F')
    
# 2. Check if the season is Autumn, Winter, Spring or Summer. 
#    If the user input is: September, October or November, the season is Autumn. 
#    December, January or February, the season is Winter. March, April or May, 
#    the season is Spring June, July or August, the season is Summer.
month = input('What is the month now?:')
season = ''
if(month == 'September' or month == 'October' or month == 'November'):
    season = 'Autumn'
elif(month == 'December' or month == 'January' or month == 'February'):
    season = 'Winter'
elif(month == 'March' or month == 'April' or month == 'May'):
    season = 'Spring'
elif(month == 'June' or month == 'July' or month == 'August'):
    season = 'Summer'
else:
    print('Please write month correctly!September,October,November,December,January,February,March,April,May,June,July,August')

print('The season is {} now.'.format(season))

# 3. The following list contains some fruits:
#    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
#    If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
one_fruit = input('Fruit:')
if(one_fruit in fruits):
    print('That fruit already exist in the list')
else:
    fruits.append(one_fruit)
    print(fruits)
#%% LEVEL - 3
# 1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Gökhan',
    'last_name': 'Arman',
    'age': 32,
    'country': 'Germany',
    'is_married': True,
    'skills': ['JavaScript', 'Node', 'Python', 'Image Processing', 'Machine Learning','React', 'MongoDB'],
    'address': {
        'street': 'SpaceX',
        'zipcode': '01905'
    }
    }
# 1A. * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# 1B. * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# 1C. * If a person skills has only JavaScript and React, print('He is a front end developer'),
#       if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#       if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#       else print('unknown title') - for more accurate results more conditions can be nested!
# 1D. * If the person is married and if he lives in Finland, 
#       print the information in the following format:

    # 1.A    
person_keys = person.keys()
print(person_keys)
import math
if('skills' in person_keys):
    skills_value = person.get('skills')
    skills_value_length = len(skills_value)
    if(skills_value_length % 2 == 1):
        middle_skill = skills_value[math.floor(skills_value_length / 2)]
        print('Middle skill:', middle_skill)
    else:
        middle_skill1 = skills_value[math.floor(skills_value_length / 2) - 1]
        middle_skill2 = skills_value[math.floor(skills_value_length / 2)]
        print('Middle skills:', middle_skill1,'and', middle_skill2)
else:
    print('No skills key in person object')

    # 1.B
if('skills' in person_keys):
    skills_value = person.get('skills')   
    if('Python' in skills_value):
        print('Python is in your skills', skills_value)
        
    # 1.C
skills_value = person.get('skills') 
if('JavaScript' in skills_value and 'React' in skills_value):
    if(len(skills_value) == 2):
        print('He is a front end developer')
    elif('React' in skills_value and 'Node' in skills_value and 'MongoDB' in skills_value):
        print('He is a fullstack developer')
elif('Node' in skills_value and 'React' in skills_value and 'MongoDB' in skills_value):
    if(len(skills_value) == 3):
        print('He is a backend developer')
else:
    print('unknown title')

    # 1.D
is_married = person.get('is_married')
country = person.get('country')
name = person.get('first_name')
surname = person.get('last_name')
print(is_married)
if(is_married == True and country == 'Germany'):
    print('{} {} lives in {}. He is married.'.format(name, surname, country))
    



    
    