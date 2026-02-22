# List and Tuples.


users = ["Dave", "Sally", "Jane", "John", "Diane"]

data = ["Dave", 42, "Sally", 43, "Jane", 44, "John", 45, "Diane", 46]

emptyList = []


print("------------------")
print("Dave" in users)
print("------------------")
print(42 in data)
print("------------------")
print("Munir" in emptyList)
print("------------------")
print(users[-3])
print("------------------")
print(users.index("Jane"))
print(users[-3:-1])
print(len(data))
users.append("Munir")
# users += data
# data.extend(["new", "List"])
print(users)
print(data)


users.insert(0, "Max")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["new", "people"]
print(users)

users.remove("Munir")
users.remove("Alex")
print(users)

users.pop()

print(users)

del users[0]
data.clear()
print(data)

users.sort()
print(users)


users.sort(key=str.lower)
print(users)


nums = [4, 40, 32, 12, 6]
# print(nums)
# nums.reverse()
# print(nums)
# # decending order nums.sort(reverse=True)
# nums.sort(reverse=True)
# print(nums)

# 3 ways to copy a list
numscopy = nums.copy

mynums = list(nums)

mycopy = nums[:]


copyofuser = users.copy

secondWayToCopy = list(users)

thirdWayToCopy = users[:]

print(nums)
# Literal reverse- no sorting.
nums.reverse()
print(nums)
# Assending sort
nums.sort()
print(nums)
# Decending sort
nums.sort(reverse=True)
print(nums)
