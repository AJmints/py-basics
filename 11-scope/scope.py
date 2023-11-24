#Scope lesson

# Reviewing global and local scope.

count = 1

def another():
    color = "blue"
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()