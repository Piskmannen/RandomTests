spam = {'list1':1,'list2':2,'list3':3}
cheese = {'list1':200,'list5':2,'list6':6}


#spam.update(cheese)
spam.setdefault(0, 1)
import pprint
if 'list1' in spam:
    #spam[1] = spam [1]+2
    spam['list1'] = spam['list1'] + cheese['list1']
else:
    print ('no')

#spam[list1] = spam[list1] + cheese[list1]
print (spam)
#if cheese[1] == spam[2]:
    #spam[2] = spam[2] + chees[1]
#pprint.pprint(spam)

