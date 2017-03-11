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

def addtolist(list):
    while result!=checklist:
        toss = random.choice(['heads','tails'])
        global count
        if toss == 'heads':
            list.append(toss)
            count += 1
        else:
            del list[:]
            count +=1
            print('no')


addtolist(result)




    
    
    #print(result)
    #if flip == 'heads':
      #  result.append(flip)
   # else:
       # del result[:]
       # continue
    


   

print('Number of attempts to get 10 heads in sequence: '+(str(count)))
