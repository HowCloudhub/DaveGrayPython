# sets
# No duplicates allowed. if duplicate values are put in, Python will
# ingnore the duplicates
# we cannot refer to an specific value with its index position.

# .update works with lists, typles, dictionaries and sets.

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(type(nums))
print(type(nums2))
print(len(nums))
print(len(nums))

# 1 is True and 0 is False
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

print(False in nums)

# add a new value to the set

nums.add(8)

print(nums)

morenums = {4, 5, 6, 7, 8, 9}

nums.update(morenums)
print(nums)

# merge 2 sets to create a new set

one = {1, 8, 3, 4, 5, 6, 7}
two = {7, 2, 9, 0, 1}

myNewSet = one.union(two)
print(myNewSet)

# this update on with only the duplicate data
one.intersection_update(two)
print(one)

one = {1, 8, 3, 4, 5, 6, 7}
two = {7, 2, 9, 0, 1}

one.symmetric_difference_update(two)
print(one)
