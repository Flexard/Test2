#10/03/2026
#Alex Bruce (ISLAND SURVIVAL)

#Library Imports

import time, sys
import random

#----Variables----

hunger = 100
health = 100

#----Functions----

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def intro(): #start of the game, giving the user context
    print("------------------------------")
    print("ISLAND ESCAPE - Text Adventure")
    print("------------------------------")

    typewriter("You wake to the sound of waves crashing against the shore.")
    print()
    typewriter("You slowly open your eyes. The last thing you remember is sailing on your boat when an extreme storm")
    print()
    typewriter("appeared out of nowhere.")
    print()
    typewriter("You find yourself lying on the warm sand of a strange island surrounded by a thick forest and")
    print()
    typewriter("towering cliffs and pieces of your boat are scattered all over the beach.")
    print()
    typewriter("But something about this island feels odd...")
    print()
    typewriter("If you want to survive and escape, you will need to explore the island in search for useful items to")
    print()
    typewriter("repair your boat.")
    print()
    typewriter("But be careful, this island is dangerous full of mysteries and surprises and not every mystery")
    print()
    typewriter("wants to be solved.")
    print()
    typewriter("YOUR GOAL IS SIMPLE:")
    print()
    typewriter("-EXPLORE THE ISLAND")
    print()
    typewriter("-FIND CLUES AND SOLVE RIDDLES TO COLLECT ITEMS")
    print()
    typewriter("-REPAIR YOUR BOAT")
    print()
    typewriter("-AND ESCAPE BEFORE IT'S TOO LATE")
    print()

def start_menu():#menu (actual start)
    print("---ISLAND ESCAPE---")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")
    response = int(input("Please enter your choice: "))
    if(response == 1):
        intro()
        loop = True
        while loop:
            loop = False
    elif(response == 2):
        print("===HOW TO PLAY===")
        print()
        print("In this text adventure game, you must explore the mysterious island, collect items, solve and discover")
        print("clues and riddles, and repair your boat to escape the island.")
        print()
        print("---MOVEMENT---")
        print()
        print("You will have to chance to explore different landmarks across the map, such as:")
        print()
        print("-Beach")
        print("-Forest")
        print("-Cave")
        print("-Temple")
        print()
        print("---INVENTORY---")
        print()
        print("As you explore the island, you will find useful items to help repair your boat.")
        print("These items are stored in your inventory.")
        print()
        print("---PUZZLES/RIDDLES---")
        print()
        print("Most area's contain puzzles and riddles.")
        print("Read the puzzles carefully, and solve them to unlock new areas around the map.")
        print()
        print("---GOAL---")
        print()
        print("Your main objective is to escape from the island.")
        print("To do this collect the boat part at each specific location.")
        print()
        print("-Rudder")
        print("-Rope")
        print("-Sail")
        print("-Engine Part")
        print()
        print("---IMPORTANT---")
        print()
        print("-Some choices will effect or health and hunger bar ")
        print("-You can restart the game whenever")
        print("-HAVE FUN!")
        print()
        response = input("Do you want to return to the main menu? (Y/N): ")
        if response == "Y" or response == "y":
                start_menu()
        elif response == "N" or response == "n":
                exit()


    elif(response == 3):
        exit()




#----Start----

start_menu()
