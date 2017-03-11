# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 11:53:43 2017

@author: Robert
"""

import random
count= 0
checklist = ('heads','heads','heads','heads','heads','heads','heads','heads','heads','heads')

result = []
flip =[]

def addtolist(list,attempt):
    while result!=checklist:
        global count
        toss = random.choice(['heads','tails'])
        if toss == 'heads':
            attempt.append(toss)
            list.append(toss)
            count += 1
        else:
            attempt.append(toss)
            del list[:]
            count +=1
    return count

x='heads','heads','heads','heads','heads','heads','heads','heads','heads','heads'

addtolist(result,flip)
print(flip)
print(result)




    
    
    #print(result)
    #if flip == 'heads':
      #  result.append(flip)
   # else:
       # del result[:]
       # continue
    


   

print('Number of attempts to get 10 heads in sequence: '+(str(count)))
