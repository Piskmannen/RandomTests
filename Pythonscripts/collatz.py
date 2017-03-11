#number = int(input("Enter a number"))
number = int(input("Enter a number"))
def collatz(number):
    global result
    if (number % 2 == 0):
        #print (number // 2)
        result= (number // 2)
        #return result
        return result
        #result = number // 2
        #return result
    else:
        #print (3*(number+1))
        
        result= (3*(number+1))
        return result
    
#result = collatz(number)
#print (result)
collatz(number)
#print (result)
while result != 1:
    collatz(int(result))
    print (result)
#


#print ('test' + (str(result)))
#print = result

#print ('testing the result variable'+(str(result)))
#print (result)

#while result != 1:
    #rint ('test')
#while collatz(number) != 1:
    #print (result (collatz(number))
           #break
    #break
#while number != 1:
    #collatz(number)
#number = int(input("Enter a number"))
#collatz(number)
#print ('result')
#while (result != 1):
    #number = int(input("Enter a number"))
    #collatz(number)
    #if number // 2 == 1:
        #break
#collatz(number)
#if (number == 1):
   # print ('Well done')
#elif:
    #collatz(number)
    #number = int(input("Enter a number"))
       # collatz(number)
       # number = int(input("Enter a number"))

