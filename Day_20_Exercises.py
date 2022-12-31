# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:16:25 2022

@author: ARMAN
"""

# 1. Read this url and find the 10 most frequent words. 
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
def find_most_frequent_words(url, number):
    import requests
       
    response = requests.get(url)    
    text = response.text    
    text_list = text.split()
    
    from collections import Counter
        
    Counter = Counter(text_list)
    
    most_frequent_words = Counter.most_common(number)
    
    return most_frequent_words
    
# print(find_most_frequent_words('http://www.gutenberg.org/files/1112/1112.txt', 10))

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

import requests
import json
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
# We can use json format
breeds = response.json()
print(breeds[1])
cats_weights = []
cats_names = []
cats_lifespan = []
for i in range(len(breeds)):
    cats_weights.append(breeds[i]['weight']['metric'])
    cats_names.append(breeds[i]['name'])
    cats_lifespan.append(breeds[i]['life_span'])
     
min_cats_weights = []
max_cats_weights = []
all_cats_weights = []
min_cats_lifespans = []
max_cats_lifespans = []
all_cats_lifespans = []
for i in range(len(cats_weights)):
    min_cats_weights.append(cats_weights[i][0])
    max_cats_weights.append(cats_weights[i][-1])
    all_cats_weights.append(cats_weights[i][0])
    all_cats_weights.append(cats_weights[i][-1])
    min_cats_lifespans.append(cats_lifespan[i][0])
    max_cats_lifespans.append(cats_lifespan[i][-1])
    all_cats_lifespans.append(cats_lifespan[i][0])
    all_cats_lifespans.append(cats_lifespan[i][-1])
    
    
# print("Weights:", all_cats_weights)
# print("Lifespans:", all_cats_lifespans)
min_cats_weights = [eval(i) for i in min_cats_weights]
max_cats_weights = [eval(i) for i in max_cats_weights]
all_cats_weights = [eval(i) for i in all_cats_weights]
# sum_cats_weights = sum(all_cats_weights)
# print("Sum Weights:", sum_cats_weights)
# cats_dict ={key:[value1, value2] for (key, value1, value2) in zip(cats_names, min_cats_weights,max_cats_weights)}

# print(cats_dict)

import statistics

cats_wmean_value = statistics.mean(all_cats_weights)
cats_wmedian_value = statistics.median(all_cats_weights)
cats_wstandard_deviation = statistics.stdev(all_cats_weights)
cats_wmin_value = min(all_cats_weights)
cats_wmax_value = max(all_cats_weights)
print("All Cats Weights Min Value:", cats_wmin_value)
print("All Cats WeightsMax Value:", cats_wmax_value)
print("All Cats WeightsMean Value:", cats_wmean_value)
print("All Cats WeightsMedian Value:", cats_wmedian_value)
print("All Cats vStandard Deviation Value:", cats_wstandard_deviation)


min_cats_lifespans = [eval(i) for i in min_cats_lifespans]
max_cats_lifespans = [eval(i) for i in max_cats_lifespans]
all_cats_lifespans = [eval(i) for i in all_cats_lifespans]

cats_lsmean_value = statistics.mean(all_cats_lifespans)
cats_lsmedian_value = statistics.median(all_cats_lifespans)
cats_lsstandard_deviation = statistics.stdev(all_cats_lifespans)
cats_lsmin_value = min(all_cats_lifespans)
cats_lsmax_value = max(all_cats_lifespans)
print("All Cats Lifespans Min Value:", cats_lsmin_value)
print("All Cats Lifespans Max Value:", cats_lsmax_value)
print("All Cats Lifespans Mean Value:", cats_lsmean_value)
print("All Cats Lifespans Median Value:", cats_lsmedian_value)
print("All Cats Lifespans Standard Deviation Value:", cats_lsstandard_deviation)









