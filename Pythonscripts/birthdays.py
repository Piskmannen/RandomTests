birthdays = {'Sasch':'Oct 16', 'Matilda':'Jan 9', 'Robert': 'Oct 14'}

while True:
    print('Enter a name: (blank to quit)')
    name=input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthdaz information for ' + name)
        print('What is their birthday?')
        bday=input()
        birthdays[name] = bday
        print('Birthday database updated')
