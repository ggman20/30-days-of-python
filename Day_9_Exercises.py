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
    
# 2. Check if the season is Autumn, Winter, Spring or Summer. 
#    If the user input is: September, October or November, the season is Autumn. 
#    December, January or February, the season is Winter. March, April or May, 
#    the season is Spring June, July or August, the season is Summer.


# 3. The following list contains some fruits:
#    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
#    If the fruit exists print('That fruit already exist in the list')


#%% LEVEL - 3

# 1. Here we have a person dictionary. Feel free to modify it!

# 1A. * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# 1B. * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# 2C. * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# 2D. * If the person is married and if he lives in Finland, print the information in the following format:
