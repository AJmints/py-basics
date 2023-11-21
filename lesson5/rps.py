import sys
import random
from enum import Enum

class RPS(Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)

playerchoice = input('Please enter a value:\n1 for ROCK\n2 for PAPER\n3 for SCISSORS\n')

player = int(playerchoice)

if player < 1 | player > 3:
   sys.exit("Greater than 1")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
   print("You win!")
elif player == 2 and computer == 1:
   print("You win!")
elif player == 3 and computer == 2:
   print("You win!")
elif player == computer:
   print("Tie Game")
else: 
   print("Python wins!")