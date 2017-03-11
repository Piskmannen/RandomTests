myPets = ['runt','flunt','scunt','munt']
print('Enter a pet name:')
name = input()
while name not in myPets:
    print('I do not have a pet named '+name)
else:
    print(name + ' is my pet.')
