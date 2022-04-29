names = []

def nameAdder():
    print('Give me a name that you would like to add to the list.')
    newName = input()
    return newName

keepAdding = 'yes'

while keepAdding == 'yes':
    names.append(nameAdder())
    print('Do you want to add another name?')
    print('Type \'yes\' if you want to add another names or anything else if you want to stop.')
    keepAdding = input()

names.reverse()

print('Your list of names is')
print(names)
