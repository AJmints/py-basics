users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
empty = []

print("Dave" in empty)
print(data[-1])
print(users.index("Sara"))
print(users[0:2]) # the index = 0, while read up to = 2. You start at the 0 index and then read the first 2 objects
print(users[1:]) # Read everything from index 1 to the end
print(users[-3:-1]) # Read from the -3 index to the -1 index
print(len(data))

users.append('Elsa')
print(users)

users += ['Jason'] # If you += "name", then you would print [ ...arr, n, a, m, e]
print(users)

users.extend(["Robert", 'Jimmy'])
print(users)
# Lines 13 && 16 && 19 are the same

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ['Eddie','Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users.sort()
print(users)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print("number: " + str(users))

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
# IN PY, nums IS A LIST, NOT AN ARRAY

# nums.sort(reverse=True)
# print(nums)

# nums.sort()
# print(nums)

print(sorted(nums, reverse=True)) # This is not sorting the actual list and leaving it alone. Global sorting list
print(nums)

# These are copies of the original nums list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
numscopy.sort()
print(numscopy)
print(mynums)
print(mycopy)

print(type(nums))

mylist = list([1, "Neil", True]) # Using the list constructor
print(mylist)


# Tuples

mytuple = tuple(("Dave", 42, True))
anothertuple = (1,3,4,7,9,2,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Niel")
newtuple = tuple(newlist)
print(newtuple)

# packing and unpacking tuples - line 90 is an example of packing a tuple
# below we are unpacking a tuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2)) # tuples have 2 methods you can call. Count requires an argument. Here we are counting the the amount of times 2 exists in "anothertuple".