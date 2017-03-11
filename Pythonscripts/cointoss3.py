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
    if result == checklist:
        break

print(result)

print('Number of attempts to get 10 heads in sequence: '+(str(count)))
 


lottonumbers = []
for i in range(52):
    lottonumbers.append(random.randint(1,53))
print('For lotto numbers:')

userinput = [int(x) for x in input('Enter 6 random digits between 1 and 52 to see how many you got right: ').split()]
#userinput=input('Enter 6 random digits between 1 and 52 to see how many you got right: ')
lottocount=0
def check_for_matches(input):
    global lottocount
    for k in input:
        #print(k)
        if k in lottonumbers:
            lottocount+=1
check_for_matches(userinput)
print(lottocount)

lottoattempts=0
def new_lottonumbers(list):
    for i in range(53):
        global lottoattempts
        list.append(random.randint(1,53))
        lottoattempts+=1
        return lottoattempts

if set(userinput)<set(lottonumbers):
    del lottonumbers[:]
    print('lottonumber should now be empty')
    print(lottonumbers)
    new_lottonumbers(lottonumbers)
    print('lottonumbers should now be full'+(str(lottonumbers)))
print('Number of times played to get a 6 number match: '+ (str(lottoattempts)))