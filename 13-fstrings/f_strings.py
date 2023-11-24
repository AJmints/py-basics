person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left" % (person, coins)
print(message)

message2 = "\n{} has {} coins left.".format(person, coins)
print(message2)

message = "\n{1} has {0} coins left".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)

player = {"person": "Dave", "coins": 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# f-strings
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 10} coins left."
print(message)

message = f"\n{player['person']} has {2*5} coins left"
print(message)

# Formatting option

num = 10
print(f"\n2.25 times {num} is {2.25*num:.2f}") # In this example, num has decimals, so we say :.2f to symbolize show 2 numbers after the decimal and f stands for fixed.

for num in range(1,11):
    print(f"2.25 times {num} is {2.25*num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")

    