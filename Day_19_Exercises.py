# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:07:52 2022

@author: ARMAN
"""

#%% LEVEL - 1
# 1.a Read obama_speech.txt file and count number of lines and words
'''
with open("./obama_speech.txt", "r") as f:
    obama_speech = f.read().splitlines()
    word_count = 0
    line_count = len(obama_speech)
    for line in obama_speech:
        obama_speech_sentences = line.split()
        # print(obama_speech_sentences)
        word_count = word_count + len(obama_speech_sentences)
        # print(word_count)

print('line count of obama_speech.txt is {} and total sentences count of obama_speech.txt is {}'.format(line_count, word_count))        
        
# 1.b Read michelle_obama_speech.txt file and count number of lines and words
with open("./michelle_obama_speech.txt", "r") as g:
    michelle_obama_speech = g.read().splitlines()
    word_count_michelle = 0
    line_count_michelle = len(michelle_obama_speech) 
    for line in michelle_obama_speech:
        michelle_obama_speech_sentences = line.split()
        word_count_michelle = word_count_michelle + len(michelle_obama_speech_sentences)

print('line count of michelle_obama_speech.txt is {} and total sentences count of michelle_obama_speech.txt is {}'.format(line_count_michelle, word_count_michelle))
        
# 1.c Read donald_speech.txt file and count number of lines and words
with open("./donald_speech.txt", "r") as h:
    donald_speech = h.read().splitlines()
    word_count_donald = 0
    line_count_donald = len(donald_speech)
    for line in donald_speech:
        donald_speech_sentences = line.split()
        word_count_donald = word_count_donald + len(donald_speech_sentences)
        
 
print('line count of donald_speech.txt is {} and total sentences count of donald_speech.txt is {}'.format(line_count_donald, word_count_donald))

# 1.d Read melina_trump_speech.txt file and count number of lines and words
with open("./melina_trump_speech.txt", "r") as j:
    melina_trump_speech = j.read().splitlines()
    word_count_melina_trump = 0
    line_count_melina_trump = len(melina_trump_speech)
    
    for line in melina_trump_speech:
        melina_trump_speech_sentences = line.split()
        word_count_melina_trump = word_count_melina_trump + len(melina_trump_speech_sentences)
        
print('line count of melina_trump_speech.txt is {} and total sentences count of melina_trump_speech.txt is {}'.format(line_count_melina_trump, word_count_melina_trump))
'''
# 2. Read the countries_data.json data file in data directory, 
#    create a function that finds the ten most spoken languages      
import json
import countries_data


data = countries_data.data # I have countries_data.py

country_json = json.dumps(data, indent = 4)

with open("./country_json.json","w",encoding = "utf-8") as f:
    json.dump(country_json, f, ensure_ascii= False, indent = 4)


def most_spoken_languages(filename, number):
    
    with open(filename) as g:           #Reading json file
        json_reader = json.load(g)
        
    country_dict = json.loads(json_reader) # Json to dictionary
    
    languages_list = []
    
    for i in range(len(country_dict)):    # Extract the languages from dict
        languages_list.append(country_dict[i]['languages'])
    
    all_lang_list = []
    
    for i in range(len(languages_list)):    # All languages 
        for lan in languages_list[i]:
            all_lang_list.append(lan)        
    
    from collections import Counter     # Using library for counter
    
    Counter = Counter(all_lang_list)
    
    most_langs = Counter.most_common(number)
    
    return most_langs
    
print(most_spoken_languages("./country_json.json", 10))

# 3. Read the countries_data.json data file in data directory, 
#    create a function that creates a list of the ten most populated countries
def most_populated_countries(filename,number):
    
    with open(filename) as g:           #Reading json file
        json_reader = json.load(g)
        
    country_dict = json.loads(json_reader)
    
    population_list = []
    
    for i in range(len(country_dict)):
        population_list.append(country_dict[i]['population'])
        
    list_of_pop = []
    for i in range(0, number):
        max1 = 0
         
        for j in range(len(population_list)):    
            if population_list[j] > max1:
                max1 = population_list[j];
                 
        population_list.remove(max1);
        list_of_pop.append(max1)
    
    country_name_list = [] 
    for population in list_of_pop:
        for i in range(len(country_dict)):
            if country_dict[i]['population'] == population: 
                country_name_list.append(country_dict[i]['name']) 
                
    last_dict = {}
    
    for key in country_name_list:
        for value in list_of_pop:
            last_dict[key] = value
            list_of_pop.remove(value)
            break
    return last_dict

print(most_populated_countries("./country_json.json", 10))

#%% LEVEL - 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
email_exchanges_big_file = './email_exchanges_big.txt'
with open(email_exchanges_big_file, "r") as f:
    email_exchanges_big = f.read().splitlines()
incoming_email_adresses = []
for i in range(len(email_exchanges_big)):
    if email_exchanges_big[i].__contains__('From:') == True and incoming_email_adresses.__contains__(email_exchanges_big[i]) == False:   
        incoming_email_adresses.append(email_exchanges_big[i])
incoming_email_adresses_without_from = []        
for i in range(len(incoming_email_adresses )):    
    incoming_email_adresses_without_from.append(incoming_email_adresses[i].replace('From: ',''))
    
print(incoming_email_adresses_without_from)              
    
# 5. Find the most common words in the English language. 
# Call the name of your function find_most_common_words, it will take two parameters - 
# a string or a file and a positive integer, indicating the number of words. 
# Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(filename, number):
    with open(filename, "r") as g:
        english_text = g.read()
    
    english_text_array = english_text.split()
            
    from collections import Counter
    
    Counter = Counter(english_text_array)
    
    most_common_word = Counter.most_common(number)
    
    return most_common_word


print(find_most_common_words("./obama_speech.txt", 10))

# 6. Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
# b) The ten most frequent words used in Michelle's speech 
# c) The ten most frequent words used in Trump's speech 
# d) The ten most frequent words used in Melina's speech

def find_most_frequent_words(filename, number):
    
    with open(filename, "r") as h:
        text6 = h.read()
        
    text6_array = text6.split()
    
    from collections import Counter 
    Counter = Counter(text6_array)
    
    most_freqeunt_words = Counter.most_common(number)
    
    return most_freqeunt_words

print("For Obama's speech:", find_most_frequent_words("./obama_speech.txt", 1))
print("For Michelle's speech:", find_most_frequent_words("./michelle_obama_speech.txt", 1))  
print("For Trump's speech:", find_most_frequent_words("./donald_speech.txt", 1))  
print("For Melina's speech:", find_most_frequent_words("./melina_trump_speech.txt", 1)) 

# 7. Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, function to clean the text(clean_text), 
# function to remove support words(remove_support_words) and 
# finally to check the similarity(check_text_similarity). List of stop words are in the data directory 

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
romeo_and_juliet_file = './romeo_and_juliet.txt'

with open(romeo_and_juliet_file, "r") as j:
    romeo_and_juliet_text = j.read()

romeo_and_juliet_list = romeo_and_juliet_text.split()


from collections import Counter

counter_romeo_and_juliet = Counter(romeo_and_juliet_list)

most_repeated_words = counter_romeo_and_juliet.most_common(10)

print('10 most repeated words in romeo and juliet:', most_repeated_words)

# 9. Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript

# I didnt access hacker news csv file

# I will write an example
import csv
with open('./csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is an electric and electronic engineer. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')









  