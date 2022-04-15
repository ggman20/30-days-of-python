# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:58:03 2022

@author: ARMAN
"""
#%% NO LEVEL
# 1. Declare your age as integer variable
age = 33

# 2. Declare your height as a float variable
height = 1.85

# 3. Declare a variable that store a complex number
is_complex = 1 + 2j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
b = 3 #base/taban
h = 5 #height/yükseklik 
area_of_triangle = 0.5 * b * h

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sidea = 5
sideb = 7
sidec = 10
perimeter_of_triangle = sidea + sideb + sidec

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)) 
length = int(input('Length:'))
width = int(input('Width:'))
area_of_rectangle = length * width
perimeter_of_rectange = 2 * (length + width)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = int(input('Radius:'))
area_of_circle = pi * (r ** 2)
circumference_of_circle = 2 * pi * r

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
x_intercept = 2 / 2
y_intercept = -2

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = ((y2-y1)/(x2-x1))
euclidean_distance = math.sqrt(((y1 - x1) ** 2) + ((y2 - x2) ** 2))
print(euclidean_distance)

# 10. Compare the slopes in tasks 8 and 9.
compare_slopes = slope - m
print('Difference slopes:', compare_slopes)
print('compare slopes', slope == m)

# 11. Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = ((x ** 2) + (6 * x) + 9)
print(y) #y = 0 when x = -3 

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('pyhton vs dragon',(len('python') == len('dragon'))) #True

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('python', 'python'.__contains__('on'))

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence_one = 'I hope this course is not full of jargon'
print('jargon', sentence_one.__contains__('jargon'))

# 15. There is no 'on' in both dragon and python
# SKIP

# 16. Find the length of the text python and convert the value to float and convert it to string
length_of_python = len('python')
length_of_python = float(length_of_python)
length_of_python = str(length_of_python)

# 17. Even numbers are divisible by 2 and the remainder is zero. 
#     How do you check if a number is even or not using python?
number = int(input('Even or Odd?:'))
print('Number is even:', number % 2 == 0) 

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('Check:',((7//3) == int(2.7))) #ITrue

# 19. Check if type of '10' is equal to type of 10
print('Check:',(type('10') == type(10)))

# 20. Check if int('9.8') is equal to 10
print((int(9.8)) == 10 )

# 21. Write a script that prompts the user to enter hours and rate per hour.
#     Calculate pay of the person?
hours = int(input('Hours:'))
rate_per_hour = int((input(' Rate per hour:')))
print('Pay of person:', hours * rate_per_hour)

# 22. Write a script that prompts the user to enter number of years. 
#     Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = int(input('Enter number of years:'))
seconds_of_years = number_of_years * 365 * 24 * 60 * 60
print('You have lived for {}'.format(seconds_of_years) + 'seconds.')

# 23. Write a Python script that displays the following table
number_for_script = int(input('Number:'))
print('{}\t'.format(number_for_script) + '1\t' + '{}\t'.format(number_for_script) + '{}\t'.format(number_for_script ** 2) + '{}\t'.format(number_for_script ** 3))


