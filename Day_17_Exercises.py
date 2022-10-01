# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 12:32:27 2022

@author: ARMAN
"""
#1. Unpack the first five countries and store them in a variable 
# nordic_countries, store Estonia and Russia in es, and ru respectively.
 
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
names.reverse()
ru, es, *nordic_countries = names
names.reverse()
print(names)
print(ru)
print(es)
print(nordic_countries)