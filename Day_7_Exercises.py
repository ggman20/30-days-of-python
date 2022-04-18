# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:14:50 2022

@author: ARMAN
"""

#%% LEVEL - 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
length_of_it_companies = len(it_companies)
print(length_of_it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(('Samsung', 'Siemens', 'Xiaomi'))
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('IBM')

# 5. What is the difference between remove and discard
# If ''our item is not found, remove method returns error but discard method does not.

#%% LEVEL - 2
# 1. Join A and B
joining = A.union(B)     #A∪B 
print(joining)

# 2. Find A intersection B
intersection = A.intersection(B)  #A/B
print(intersection)

# 3. Is A subset of B
print('A is subset of B:', A.issubset(B)) #A, B2'nin alt kümesi mi? --> True

# 4. Are A and B disjoint sets
print('A and B are disjoint:', A.isdisjoint(B)) #A ve B kümeleri ayrık kümeler mi? --> False

# 5. Join A with B and B with A
# A.update(B)
# print(A)

# 6. What is the symmetric difference between A and B
symmetric_difference_of_A_B = A.symmetric_difference(B)
print(symmetric_difference_of_A_B) # (A\B) ∪ (B\A)

# 7. Delete the sets completely
del A
del B

#%% LEVEL - 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
length_set_age = len(set_age)
length_list_age = len(age)
difference_of_list_and_set_ages = abs(length_list_age - length_set_age)
if(length_list_age - length_set_age > 0):
    print('List is bigger than set and difference is {}.'.format(difference_of_list_and_set_ages))
else:
    print('Set is bigger than list and difference is {}.'.format(difference_of_list_and_set_ages))
# 2. Explain the difference between the following data types: string, list, tuple and set
#       SKIP

# 3. 'I am a teacher and I love to inspire and teach people.' 
#    How many unique words have been used in the sentence? 
#    Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
set_sentence = set(sentence.split(' '))
print(set_sentence)
length_set_sentence = len(set_sentence)
print('There are {} unique words in this sentence: '.format(length_set_sentence))

