inventory = {'rope': 1, 'torch': 4, 'gold coin': 9, 'dagger': 2, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print('Inventory:')
def addToInventory():
    for k in dragonLoot:
        if k in inventory.keys():
            inventory[k] += 1

for k,v in inventory.items():
    print (str(v)+' ' +k)
    
sum = sum(inventory.values())

print (('Total number of items:')+' '+(str(sum)))



answer = input('Add Dragon Loot to inventory? Yes or no? ')
if answer == 'yes' or 'Yes':
    addToInventory()
    print ('Updated Inventory:')
    for k,v in inventory.items():
        print (str(v)+' ' +k)

