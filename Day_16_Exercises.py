# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:24:58 2022

@author: ARMAN
"""
#%% LEVEL -1
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print('day = {}, month = {}'.format(day, month))

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime
now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

# 3.Today is 5 December, 2019. Change this time string to time.
from datetime import datetime
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 4.Calculate the time difference between now and new year.
from datetime import datetime
t1 = datetime(year, month, day, hour, minute)
t2= datetime(year = 2023, month = 1, day = 1, hour = 0, minute =0)
difference = t2 - t1
print(difference)
# 5.Calculate the time difference between 1 January 1970 and now.
t3 = datetime(year = 1970, month = 1, day = 1)
t4 = datetime(year, month, day)
difference_between_timestamp = t4 - t3
print(difference_between_timestamp)

# 6.Think, what can you use the datetime module for?
#I can use the datatime module for past time for my application with timestamp
    
