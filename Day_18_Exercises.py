# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:25:09 2022

@author: ARMAN
"""

#%% LEVEL - 1
#1. What is the most frequent word in the following paragraph?

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re

divide = re.split('\s', paragraph)
a = []
# print(divide)

different_words = list(set(divide))
# print(b)
for word in different_words:
    a.append(re.findall(word,paragraph))

arr = []
for i in a:
    arr.append(len(i))
  
print(arr)


  

