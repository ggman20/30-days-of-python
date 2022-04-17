# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:22:17 2022

@author: ARMAN
"""
#%% NO LEVEL
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + 'Days' + 'Of' + 'Python')

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' + 'For' + 'All')

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
first_word_company = company[0:6]
print(first_word_company)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print(company.__contains__('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
python_company = company.replace('Coding', 'Python')
print(python_company)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print('Python for Everyone'.replace('Everyone','All'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
array_company = company.split()
print(array_company)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
array_big_companies = big_companies.split(',')
print(array_big_companies)

# 15. What is the character at index 0 in the string Coding For All.
index_0_for_company = company[0]
print(index_0_for_company)

# 16. What is the last index of the string Coding For All.
last_index_for_company = company[-1]
print(last_index_for_company)

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_for_everyone = 'Python For Everyone'
array_python_for_everyone = python_for_everyone.split()
pfe = array_python_for_everyone[0][0] + array_python_for_everyone[1][0] + array_python_for_everyone[2][0]
print(pfe) #PFE

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = array_company[0][0] + array_company[1][0] + array_company[2][0]
print(cfa) #CFA

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
#     'You cannot end a sentence with because because because is a conjunction'
because_sentence = 'You cannot end a sentence with because because because is a conjunction'
because_index1 = because_sentence.index('because')

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
#     'You cannot end a sentence with because because because is a conjunction'
because_index_last = because_sentence.rindex('because')

# 25. Slice out the phrase 'because because because' in the following sentence: 
#     'You cannot end a sentence with because because because is a conjunction'
all_because = because_sentence[(because_index1):(because_index_last + len('because'))]
print(all_because) #because because because

# 26. Find the position of the first occurrence of the word 'because' in the following sentence:
#     'You cannot end a sentence with because because because is a conjunction'
because_find1 = because_sentence.find('because') 
print(because_find1)

# 27. Slice out the phrase 'because because because' in the following sentence:
#     'You cannot end a sentence with because because because is a conjunction'
because_find_last = because_sentence.rfind('because')
all_because_with_find = because_sentence[(because_find1):(because_find_last + len('because'))]
print(all_because_with_find)

# 28. Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip('   '))

# 31. Which one of the following variables return True when we use the method isidentifier():
print(company.isidentifier())
print('CodingForAll'.isidentifier())

# 32. The following list contains the names of some of python libraries: 
#     ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
mix_array = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
mix_string = ' '.join(mix_array)
print(mix_string)

# 33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Gökhan\t33\tGermany\tBerlin')

# 35. Use the string formatting method to display the following:
name = 'Gökhan'
surname = 'Arman'
age = 33
print('I am {} {} and my age is {}'.format(name,surname,age))

# 36. Make the following using string formatting methods:
number1 = 8
number2 = 6
print('{} + {} = {}'.format(number1, number2, (number1 + number2)))
print('{} - {} = {}'.format(number1, number2, (number1 - number2)))
print('{} * {} = {}'.format(number1, number2, (number1 * number2)))
print('{} / {} = {:.2f}'.format(number1, number2, (number1 / number2)))
print('{} % {} = {}'.format(number1, number2, (number1 % number2)))
print('{} // {} = {}'.format(number1, number2, (number1 // number2)))
print('{} ** {} = {}'.format(number1, number2, (number1 ** number2)))
   
