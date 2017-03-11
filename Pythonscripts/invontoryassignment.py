inventory = {'rope': 1, 'torch': 4, 'gold coin': 9, 'dagger': 2, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin' 'ruby']
print('Inventory:')
def addToInventory():
    for k, v in inventory.items():
        for i in dragonLoot:
            # findCount = 0
            if i == k:
                print ('amount of gold coin is', + sum(inventory.["gold coin"]))
                inventory.update()
            else:
                print ("(i)", 'is NOT equal to (k) or not found')
               # inventory.values = inventory.values + (int(1))
               # findCount += 1
            #if findCount == 0:
                #inventory.values = 1
    #inventoryUpdated = dict(inventory.items() + dragonLoot.item())
    #if dragonLoot.items not in inventory.items():
       # print ('inventory needs to be updated')
#addToInventory()
for k,v in inventory.items():
    print (str(v)+' ' +k)
    
    
sum = sum(inventory.values())

print (('Total number of items:')+' '+(str(sum)))



answer = input('Add Dragon Loot to inventory? Yes or no?')
if answer == 'yes' or 'Yes':
    addToInventory()
    print ('Updated Inventory:')
    for k,v in inventory.items():
        print (str(v)+' ' +k)
    
else:
    print ('failed for some reason')
    #print ('this should launch the function')

