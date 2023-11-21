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
print(users)