spam=['apples','bananas','tofu','cats','moose','goose']
cheese=['coins','rubber','oil','misery']
#Result=((spam[0:3])+(str('and')) +spam[3])
#print (str(' '.join.spam[0:3])+('and'))
#Type=input() 

print (str.join(', ',(spam[0:-1]))+(' and ')+spam[-1])
