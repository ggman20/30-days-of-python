# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:53:02 2022

@author: ARMAN
"""
#%% Pre-exercising from lesson day-2
# first_name = input('What is your name: ')
# print(first_name)
#%% LEVEL-1
# 1. Inside 30DaysOfPython create a folder called day_2. 
#    Inside this folder create a file named variables.py
#SKIP

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
print('Day 2: 30 Days of python programming')

# 3. Declare a first name variable and assign a value to it
first_name = 'Gökhan'

# 4. Declare a last name variable and assign a value to it
last_name = 'Arman'

# 5. Declare a full name variable and assign a value to it
full_name = first_name + last_name

# 6. Declare a country variable and assign a value to it
country = 'Germany'

# 7. Declare a city variable and assign a value to it
city = 'Berlin'

# 8. Declare an age variable and assign a value to it
age = 33

# 9. Declare a year variable and assign a value to it
year = 2022

# 10. Declare a variable is_married and assign a value to it
is_married = True

# 11. Declare a variable is_true and assign a value to it
is_true = True

# 12. Declare a variable is_light_on and assign a value to it
is_light = True

# 13. Declare multiple variable on one line
first_name, last_name, country = 'Gökhan', 'Arman', 'Germany'
#%% LEVEL-2
# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

# 2. Using the len() built-in function, find the length of your first name
print('first name length:', len(first_name))

# 3. Compare the length of your first name and your last name
print('First name length:', len(first_name), 'Last name length:', len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
total = num_one + num_two #Add num_one and num_two and assign the value to a variable total
diff = num_two - num_one #Subtract num_two from num_one and assign the value to a variable diff
product = num_two * num_one #Multiply num_two and num_one and assign the value to a variable product
division = num_one / num_two #Divide num_one by num_two and assign the value to a variable division
remainder = num_two % num_one #Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exp = num_one ** num_two #Calculate num_one to the power of num_two and assign the value to a variable exp
floor_division = num_one // num_two #Find floor division of num_one by num_two and assign the value to a variable floor_division
print('total:',total, 'diff:', diff, 'product:', product, 'division:', division,
      'remainder:', remainder, 'exp:', exp, 'floor division:', floor_division
      )

# 5. The radius of a circle is 30 meters.
pi = 3.14
r = 30
area_of_circle = pi * (r ** 2) #Calculate the area of a circle and assign the value to a variable name of area_of_circle
circum_of_circle = 2 * pi * r #Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
input_r = int(input('radius:'))
area_of_circle_2 = pi * (input_r ** 2)
print("Area1:",area_of_circle, "Circumference:", circum_of_circle, "Area2:", area_of_circle_2)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names.
first_name_input = input('First name:')
last_name_input = input('Last name:')
country_input = input('Country:')
age_input = int(input('Age:'))
first_name = first_name_input
last_name = last_name_input
country = country_input 
age = age_input

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# DONE!
