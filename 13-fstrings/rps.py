import sys
import random
from enum import Enum


def rps():
   game_count = 0
   player_wins = 0
   python_wins = 0

   def play_rps():
      nonlocal player_wins
      nonlocal python_wins

      class RPS(Enum):
         ROCK = 1
         PAPER = 2
         SCISSORS = 3

      playerchoice = input('\nPlease enter a value:\n1 for ROCK\n2 for PAPER\n3 for SCISSORS\n')
      
      if playerchoice not in ["1", "2", "3"]:
         print("You must enter 1, 2, or 3.")
         return play_rps()
      
      player = int(playerchoice)

      computerchoice = random.choice("123")

      computer = int(computerchoice)

      print(f"\nYou chose {str(RPS(player)).replace('RPS.','')}.")
      print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

      def decide_winner(player, computer):
         nonlocal player_wins
         nonlocal python_wins

         if player == 1 and computer == 3:
            player_wins += 1
            return "You win!"
         elif player == 2 and computer == 1:
            player_wins += 1
            return "You win!"
         elif player == 3 and computer == 2:
            player_wins += 1
            return "You win!"
         elif player == computer:
            return "Tie Game"
         else: 
            python_wins += 1
            return "Python wins!"
         
      game_result = decide_winner(player, computer)
      print(str(game_result))

      nonlocal game_count
      game_count += 1

      print(f"\nGame count: {str(game_count)} \nPlayer wins: {str(player_wins)} \nPython wins: {str(python_wins)}")
 
      print("\nPlay again?")

      while True:

         playagain = input("\nY for yes or Q to quit \n")
         if playagain.lower() not in ["y", "q"]:
            continue
         else:
            break

      if playagain.lower() == "y":
         return play_rps()
      else:
         print("\nThank you for playing!\n")
         sys.exit("See you later!")

   return play_rps

play = rps()

play()