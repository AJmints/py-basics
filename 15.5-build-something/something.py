# Make my own little terminal game
import sys
import random


def something():

    print("something")
    random_num = random.choice("123456789")
    print(random_num)
    if random_num > 5:
        print("Nice")
    elif random_num < 3:
        print("Also nice...")
    else:
        print("4 or 5, less than 6")


something()