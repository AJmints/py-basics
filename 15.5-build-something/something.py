# Make my own little terminal game
import sys
import random

def something():
    print("something")
    randomNum = random.choice("123456789")
    print(randomNum)
    if randomNum > 5:
        print("Nice")
    elif randomNum < 2:
        print("Also nice...")
    else:
        print("3, 4 or 5")

something()