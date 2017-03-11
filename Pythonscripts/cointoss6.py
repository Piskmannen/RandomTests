# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:05:06 2017

@author: Robert
"""
import random
x=[]
z=['heads','heads','heads','heads','heads','heads','heads','heads','heads','heads',]
count = 0
def addtolist(list):
    while x!=z:
        toss = random.choice(['heads','tails'])
        if toss == 'heads':
            list.append(toss)
            global count
            count +=1
        else:
            del list[:]
            count +=1
            print('no')

addtolist(x)
print('Number of attempts needed to get 10 heads in sequence: '+(str(count)))

print('For Lotto:\n A random 6 sequence number is generated, and is then tested against a 52 number grid, to see how many times it needs to randomiye before it hits a grid with all 6 numbers')

lottopicks = []
lottogrid = list(range(52+1))
lottonumbers = [random.sample(range(53), 6)]
lottocount = 0
success = 0
def check_for_matches(list,picks):
    global lottocount
    global success
    while (success < 6):
        lottopicks.append(random.sample(range(53), 6))
        lottonumbers.append(random.sample(range(53), 7))
        for k in list:
            if k in picks:
                print('zes')
                success +=1
                lottocount+=1
            else:
                print('no')
                del list[:]
                del picks[:]
                continue
            
     
#check_for_matches(lottopicks,lottonumbers)
def lotto(list,picks):
    picks.append(random.sample(range(53), 7))
    print('lottopicks first iteration'+(str(picks)))
    while all(x in [list] for x in [picks]):
        print('yes')
        break
    else:
        print('no')
        del picks[:]
        print('lottopicks after deletion: '+(str(picks)))
        picks.append(random.sample(range(53), 7))
        print('lottopicks second iteration: '+(str(picks)))
        global count
        count +=1
   
        #if list in picks:
        #    break
        #else:
        #    continue
lottopicks.append(random.sample(range(53), 7))

while all(x in [lottonumbers] for x in [lottopicks]):
    print('yes')
    break
else:
    print('no')
    del lottopicks[:]
    print('lottopicks after deletion: '+(str(lottopicks)))
    lottopicks.append(random.sample(range(53), 7))
    print('lottopicks second iteration: '+(str(lottopicks)))
    lottocount +=1
    continue
            
print('Lotto numbers: '+(str(lottonumbers)))
#lotto(lottonumbers,lottopicks)