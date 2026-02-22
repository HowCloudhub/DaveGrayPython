
mytuple = tuple(('Munir', 42, True))
myNewTuple = tuple(('alex', 'adrian', 'aaron', 'sophie'))
numTuple = (1, 3, 4, 3, 2, 4, 9)

print(myNewTuple)
print(numTuple)

print(type(myNewTuple))
print(type(numTuple))


newList = list(myNewTuple)
newList.append('munir')
newList[0:0] = ['shahida']
newtuple = tuple(newList)
numTuple2 = (1, 2, 4, 2)

print(newList)
print(newtuple)

# Unpacking a tuple
(mom, *kids, dad) = newtuple

print(mom)
print(dad)
print(kids)

# check how many times something show up in a tuple
print(numTuple.count(2))
