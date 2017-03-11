# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 11:53:43 2017

@author: Robert
"""

import random
count= 0
checklist = ['heads','heads','heads','heads','heads','heads','heads','heads','heads','heads']

result = []






def addtolist(dict):
    dict.append(random.choice(['heads','tails']))
    global count
    count += 1
    return count

 
for i in range(10):
    addtolist(result)


    
while result != checklist:
    del result[:]
    for i in range(10):
        addtolist(result)
    if result == checklist2:
        break

print(result)
print('Number of attempts to get 10 heads in sequence: '+(str(count)))
 
lottonumbers = []
for i in range(52):
    lottonumbers.append(random.randint(1,53))
print('For lotto numbers:')
userinput=input('Enter 6 random digits between 1 and 52 to see how many you got right: ')