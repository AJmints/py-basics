import sys
import random
from enum import Enum

class RPS(Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

playagain = True

while playagain:
   playerchoice = input('\nPlease enter a value:\n1 for ROCK\n2 for PAPER\n3 for SCISSORS\n')
   player = int(playerchoice)

   if player < 1 | player > 3:
      sys.exit("You must enter 1, 2, or 3.")

   computerchoice = random.choice("123")

   computer = int(computerchoice)

   print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
   print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

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

   playagain = input("\nPlay again? \nY for yes or Q to quit \n\n")

   if playagain.lower() == "y":
      continue
   else:
      print("congrats!")
      print("Thank you for playing!\n")
      playagain = False
      # break

sys.exit("See you later!")