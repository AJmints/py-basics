from random import choice

capital = "Tokeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"

def randomfunfacts():
    funfacts = [
        "Kansas", "is", "a", "state"
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfacts()