import pprint
spam = {'list1':1,'list2':2,'list3':3}
#print (spam)
cheese = ['list1','list1','list1','list5']

#print (cheese)
#print ("Length of Cheese as a set = {0}".format(len(cheese)))

# !!-- faulty function. copy for item code block below)
def printInventory(inventory):
    print('Inventory:')
    for k,v in spam:
        k = spam.keys
        print (k)
printInventory(inventory)

#!--

#print (cheese)
#print ("Length of Cheese as a list = {0}".format(len(cheese)))

for item in cheese:
    findCount = 0
    for key, val in  iter(spam.items()):
        if item == key:
            spam[item] = spam[item] + 1
            findCount += 1
    if findCount == 0:
        spam[item] = 1
#print ("Running function to add list items to dictionary")
#print (spam)
print (('Amount of items in inventory:') + ' ' + (str(sum(spam.values()))))
#pprint.pprint(spam)
