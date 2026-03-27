#10/03/2026
#Alex Bruce (ISLAND SURVIVAL)

#Library Imports

import time, sys
import random


#----Variables----

player_name = ""
inventory = []
hunger = 100
health = 100

#----Functions----




def check(q):
    while True:
        try:
            value1 = int(input(q))
        except:
            print("Error: Enter a number")
        else:
            if value1 < 1 or value1 > 3:
                print("Error: Out of range")
            else:
                return value1

def check2(q):
    while True:
        try:
            value1 = int(input(q))
        except:
            print("Error: Enter a number")
        else:
            if value1 < 1 or value1 > 4:
                print("Error: Out of range")
            else:
                return value1

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0008) #good reading speed (0.08)

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
    print()
    print("---ISLAND ESCAPE---")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")
    response = check("Please enter your choice: ")
    if(response == 1):
        intro()
        loop = True
        while loop:
            loop = False
    elif(response == 2):
        print()
        print("===HOW TO PLAY===")
        print()
        typewriter("In this text adventure game, you must explore the mysterious island, collect items, solve and discover")
        print()
        typewriter("clues and riddles, and repair your boat to escape the island.")
        print()
        print()
        print("---MOVEMENT---")
        print()
        typewriter("You will have to chance to explore different landmarks across the map, such as:")
        print()
        print("-Beach")
        print("-Forest")
        print("-Cave")
        print("-Temple Ruins")
        print()
        print("---INVENTORY---")
        print()
        typewriter("As you explore the island, you will find useful items to help repair your boat.")
        print()
        typewriter("These items are stored in your inventory.")
        print()
        print()
        print("---PUZZLES/RIDDLES---")
        print()
        typewriter("Most area's contain puzzles and riddles.")
        print()
        typewriter("Read the puzzles carefully, and solve them to unlock new areas around the map.")
        print()
        print()
        print("---GOAL---")
        print()
        typewriter("Your main objective is to escape from the island.")
        print()
        typewriter("To do this collect the boat part at each specific location.")
        print()
        print("-Rudder")
        print("-Steering Wheel")
        print("-Sail")
        print("-Engine Part")
        print()
        print("---IMPORTANT---")
        print()
        typewriter("-Some choices will effect or health and hunger bar ")
        print()
        typewriter("-You can restart the game whenever")
        print()
        typewriter("-HAVE FUN!")
        print()
        print()
        response = input("Do you want to return to the main menu? (Y/N): ")
        if response == "Y" or response == "y":
                start_menu()
        elif response == "N" or response == "n":
                exit()


    elif(response == 3):
        exit()

def riddles():
    riddles = [
        {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
        {"question": "I am always in front of you, but can never be seen. What am I?", "answer": "the future"}
    ]

    riddle = random.choice(riddles)

    print(riddle["question"])
    answer = input("Your answer: ").lower()

    if answer == riddle["answer"]:
        print("Correct!- The chest opens.")
        return True

    else:
        print("Wrong answer. The chest stays locked.")
        return False




def movement():
    print("Where would you like to explore?")
    print("1. Beach")
    print("2. Forest")
    print("3. Cave")
    print("4. Temple Ruins")
    response = check2("Please enter your choice: ")

    if(response == 1):
        beach()

    elif(response == 2):
        forest()

    elif(response == 3):
        cave()

    elif(response == 4):
        temple()

def beach():
    typewriter("You choose to stay at the beach, explore the wreckage for a rudder to repair your boat.")
    print()
    response = input("Search for the rudder? Y/N:")

    if response == "Y" or response == "y":
            print()
            typewriter("The storm had just passed, leaving the beach scattered with boat debris. Your boat was wreaked, and you")
            print()
            typewriter("couldn't leave.")
            print()
            typewriter("After exploring the debris, you notice the rudder wedged between some rocks.")
            print()
            typewriter("And the only way you can get it out is by finding the hammer inside your tool chest to break the rocks.")
            print()
            typewriter("As your walking, ")
            beach_event()
            print()
            typewriter("But to open the chest you need to solve a riddle:")
            print()
            result = riddles()

            if result:
                print("You found a hammer!")
                inventory.append("hammer")
            else:
                movement()



    elif response == "N" or response == "n":
            movement()

def forest():
    print("HI")
def cave():
    print("Hello")
def temple():
    print("Yes")

def beach_event():
    event = random.randint(1,3)

    if event == 1:
        typewriter("you find water.")
        inventory.append("water")
        print()
        print(inventory)
        typewriter("And right next to it is your tool chest")

    elif event == 2:
        typewriter("you step on sharp glass!")
        global health
        health -= 10

    else:
        typewriter("you find your tool chest.")

#----Start----

start_menu()
print()
movement()
