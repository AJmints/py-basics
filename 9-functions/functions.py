def hello_world():
    print("Hello world!")

hello_world()

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum("a", 99)
print(sum(3, 9))
print(total) # None is like undefined, or null?

def multiple_items(*args):
    print(args)
    print(type(args))
    return

multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs): # kwargs = key word arguments
    print(kwargs)
    print(type(kwargs))
    return

mult_named_items(first="John", last="Sara")