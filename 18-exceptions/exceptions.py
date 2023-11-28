# Py exceptions are "Raised" not "Thrown"

# 5. Custom errors
class JustNotCoolError(Exception):
    pass

x = 2

try:
    # 1.
    # print(y)
    # 2.
    print(x / 0)
    # 3.
    # print(x / 1)
    # 4.
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
    # 5.
    # raise JustNotCoolError("This isn't cool, dawg")

    # raise Exception("I'm a custom exception")
except NameError:
    print("1. NameError means something is probably undefined")
except ZeroDivisionError:
    print("2. Please do not divide by zero")
except Exception as error:
    # 4.
    print(error)
else:
    print("3. No Errors!")
finally:
    print("I'm going to print regardless")