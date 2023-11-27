# Make my own little terminal game
import sys
import random
from rps import rps


def something():


    name = input("\nHello, welcome to a console game. Please enter your name.\n")

    def game_time():
        global returning_player
        returning_player = False
        while True:
            if returning_player == True:
                print(f".....\n...\nWelcome back {name}.")

            if name == "":
                correct_input = True
                while correct_input:
                    try_name = input("Please enter your name.\n")
                    if try_name != "":
                        break

            game = input(f"\nAlright, {name}.\nPlease enter a number corresponding to the game you'd like to play.\n\n1. Rock Paper Scissors\n2. Game Time\n3. Exit\n")
            if game == "1":
                rps_game = rps(name)
                rps_game()
            if game == "2":
                print("Other game file...\n")
            if game == "3":
                print("Thank you for playing!")
                return

            returning_player = True

    game_time()

something()