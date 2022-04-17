# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:04:43 2022

@author: ARMAN
"""

#%% LEVEL - 1
# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
a_lot_of_items = ['Gökhan', 'Germany', 'now', 33, 'USA', 'Berlin', 2024]

# 3. Find the length of your list
print("Length of array:", len(a_lot_of_items))

# 4. Get the first item, the middle item and the last item of the list
print("First item:", a_lot_of_items[0])
import math
length_a_lot_of_items = len(a_lot_of_items)
print("Middle item:", a_lot_of_items[math.floor(length_a_lot_of_items/2)])
print("Last item:", a_lot_of_items[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Gökhan', 33, 1.85, True, 'Denizli']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print("First company:",it_companies[0])
print("Middle company:", it_companies[math.floor(len(it_companies)/2)])
print("Last company:", it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Instagram'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Samsung')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
middle_index_for_it_companies = math.floor(len(it_companies)/2)
print(middle_index_for_it_companies)
it_companies.insert(middle_index_for_it_companies, 'Siemens')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
string_it_companies = '#;  '.join(it_companies)
print(string_it_companies)

# 15. Check if a certain company exists in the it_companies list.
company_exists = 'Siemens' in it_companies
print(company_exists)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_3_it_companies = it_companies[0:3]
print(first_3_it_companies)

# 19. Slice out the last 3 companies from the list
last_3_it_companies= it_companies[-4:-1]
print(last_3_it_companies)

# 20. Slice out the middle IT company or companies from the list
length_a_lot_of_items = len(it_companies)
print(length_a_lot_of_items % 2 == 0)
middle_index_of_it_companies = math.floor(length_a_lot_of_items/2)
middle_company_of_it_companies = it_companies[middle_index_of_it_companies]
print(middle_company_of_it_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(math.floor(len(it_companies)/2))
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(len(it_companies) - 1)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
    
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.append('Redux')
full_stack.insert((len(full_stack)), 'Python')
full_stack.insert((len(full_stack)), 'SQL')
print(full_stack)

#%% LEVEL - 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    
# 1A. Sort the list and find the min and max age
ages.sort()
# 1B. Add the min age and the max age again to the list
min_age = ages[0]
max_age = ages[-1]
ages.insert(0, min_age)
ages.insert(len(ages), max_age)
print(ages)

# 1C. Find the median age (one middle item or two middle items divided by two)
length_ages = len(ages)
print()

if(length_ages % 2 == 1):
    middle_age = ages[math.floor(length_ages / 2)]
    print("Median age:", middle_age)
else:
    middle_age1 = ages[math.floor(length_ages / 2)] 
    middle_age2 = ages[math.floor(length_ages / 2) + 1]
    print('Median ages:', middle_age1, 'and', middle_age2)

# 1D. Find the average age (sum of all items divided by their number )
sum_age = 0

for i in range(length_ages):
    sum_age = sum_age + ages[i]

average_age = sum_age / length_ages
print("Average age:", average_age)

# 1E. Find the range of the ages (max minus min)
range_of_ages = int(ages[-1]) - int(ages[0])
print('Range of age:', range_of_ages)

# 1F. Compare the value of (min - average) and (max - average), use abs() method
min_diff_average = abs(ages[0] - average_age)  
max_diff_average = abs(ages[-1] - average_age)
print('Min difference average:', min_diff_average)
print('Max diff average:', max_diff_average)

# 2. Find the middle country(ies) in the countries list
import countries
countries_from_countries = countries.countries.copy()
print(countries_from_countries)
length_of_countries = len(countries_from_countries)
print(length_of_countries)
if (length_of_countries % 2 == 1):
    middle_country = countries_from_countries[math.floor(length_of_countries / 2)]
    print('Middle Country:', middle_country)
    print('Middle country is {}. \nWe have only one middle country.\nBecause of length of countries is {} so it is odd number.'.format(middle_country, length_of_countries  ))
else:
    middle_country1 = countries_from_countries[math.floor(length_of_countries / 2)]
    middle_country2 = countries_from_countries[math.floor(length_of_countries / 2) + 1]
    print(middle_country1)
    print(middle_country2)
    print('Middle countries are {} and {}.\n Because of length of countries is {} so it is even number.'.format(middle_country1, middle_country2, length_of_countries  ))

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
if(length_of_countries % 2 == 0):
    print('0')
    first_half = countries_from_countries[0: len(countries_from_countries) / 2]
    print(len(first_half), first_half)
    second_half = countries_from_countries[len(countries_from_countries) / 2:]
    print(len(second_half), second_half)
else:
    print('1')
    first_half = countries_from_countries[0: math.floor(len(countries_from_countries) / 2)]
    first_half.append('GALATASARAY')
    print(len(first_half), first_half)
    second_half = countries_from_countries[math.floor(len(countries_from_countries) / 2): ]
    print(len(second_half), second_half)
    
# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
some_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, usa, *scandic = some_countries
print(ch)
print(ru)
print(usa)
print(scandic)
    