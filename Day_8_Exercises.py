# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:18:27 2022

@author: ARMAN
"""
#%% NO LEVEL
# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
       'name' : 'Harry',
       'breed': 'golden',
       'legs' :'tall',
       'age' : 3
       }
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first name' : 'Mustafa',
    'last_name' : 'Işık',
    'gender' : 'male',
    'age' : 15,
    'marital_status' : 'single',
    'skills' : ['football', 'video games'],
    'country' : 'Turkey',
    'city' : 'İzmir',
    'address' : {
        'street' : 'Degirmen',
        'apt' : 'Erdal',
        'no' : 10,
        'zipcode' : 35035
        }
    }
print(student)

# 4. Get the length of the student dictionary
print('Length of the student dictionary is {}'.format(len(student)))

# 5. Get the value of skills and check the data type, it should be a list
skills_values = student.get('skills')
print(type(skills_values)) 

# 6. Modify the skills values by adding one or two skills
student['skills'].append('math')
student['skills'].append('english')
print(student['skills'])

# 7. Get the dictionary keys as a list
student_keys = student.keys()
print('Keys', student_keys)

# 8. Get the dictionary values as a list
student_values = student.values()
print('Values', student_values)

# 9. Change the dictionary to a list of tuples using items() method
list_student = student.items()
print('LIST', list_student)

# 10.Delete one of the items in the dictionary
student.pop('skills')
print(student)

# 11.Delete one of the dictionaries
del dog



