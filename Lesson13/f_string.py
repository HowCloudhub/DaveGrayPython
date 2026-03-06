person = 'Dave'
coins = 3

print('\n' + person + ' has' + str(coins) + ' coins left.')

# %s methon
message = "\n%s has %s coins left." % (person, coins)
print(message)

# .format version
message = "\n{} has {} coins left.".format(person, coins) 
print(message)

# .format version with indexing
message = "\n{1} has {0} coins left.".format(coins, person) 
print(message)

# .format version with assignment 
message = "\n{person} has {coins} coins left.".format(coins =coins, person = person) 
print(message)

# .format version with dictionary 
player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left.".format(**player) 
print(message)

for num in range(1,11):
    print (f"9 times {num} is {num * 9}  ")
    print("*****************")