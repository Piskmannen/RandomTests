import sys

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    #else:
        print('that wasnt right. try again')
    print('You typed '+response +'.')
