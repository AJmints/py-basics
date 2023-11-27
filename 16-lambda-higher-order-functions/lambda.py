# Lambda = anonymous function

squared = lambda num : num * num

print(squared(2))

add_two = lambda num : num + 2

print(add_two(9))

add_multiple = lambda num, num2 : num + num2
# def add_multiple(num, num2): return num + num2

print(add_multiple(3, 5))

# When to use a lambda?

def funcBuilder(x):
    return lambda num : num + x

add_ten = funcBuilder(10) # Setting x by calling funcBuilder
add_twenty = funcBuilder(20)

print(add_ten(1)) # lambda is being called when calling add_ten filling in num
print(add_twenty(1))

# Higher order functions / map func

numbers = [3, 7, 12, 18, 20, 21, 45, 99, 111, 1]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

# Lambda filter

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

# Lambda

from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
print(sum(numbers, 10))
# The example above shows that sum is the better function vs reduce

names = ["Alex J", "Sara Ito", "Noi Big Namefor something"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)
# The above function is a better example of reduce/ higher level function