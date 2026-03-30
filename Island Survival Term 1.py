#10/03/2026
#Alex Bruce (ISLAND SURVIVAL)

#Library Imports

import time, sys    #for typewriter function
import random       #for random events in the game


#----Variables----

inventory = []      #players inventory
health = 100        #players health
visited = set()     #keep track of what the user explored locations
required_items = {"Rudder", "Keel", "Sail", "Engine Part"} #items needed to repair the boat

#----Functions----


def health_bar():
    global health

    if health <= 0 or health < 10:
        print(f"Health: {health}/100")
        print("You ran out of health. GAME OVER!")
        start_menu()  #go back to start menu
        return

    # Visual Health Bar
    bar_length = 10

    filled = int((health / 100) * bar_length)
    empty = bar_length - filled

    bar = "⬜" * filled + "⬛" * empty
    print(f"Health: [{bar}]{health}/100")


def check(q): #function for start multi-choice
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

def check2(q): #function for movement multi-choice
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

def check3(q): #function for Y/N multi-choice
    while True:
        value1 = input(q).strip().lower()

        if value1 == "y" or value1 == "n":
            return value1
        else:
            print("Error: Try again")

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08) #good reading speed (0.08)


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
    typewriter("YOUR GOAL IS SIMPLE:") #tells the user the goal
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
    if response == 1:
        intro()
        # Startthe main game loop
        loop = True
        while loop:
            loop = False # Stops immediately, goes back to movement
    elif response == 2:
        print()
        print("===HOW TO PLAY===") # instructions for the game
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
        print("-Keel")
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
        response = check3("Do you want to return to the main menu? (Y/N): ")
        if response == "Y" or response == "y":
                start_menu()
        elif response == "N" or response == "n":
                exit()


    elif(response == 3):
        exit() # quit the game

def riddles():
    global health
    riddles = [
        {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
        {"question": "I am an odd number. Take away a letter and I become even. What number am I?", "answer": "seven"},
        {"question": "What is always on its way but never arrives?", "answer": "tomorrow"},
        {"question": "Poor people have it. Rich people need it. If you eat it you die. What is it?", "answer": "nothing"},
        {"question": "What can fill a room without taking up any space?", "answer": "light"},
        {"question": "Forward, it's heavy. Backward, it's not. What is it?", "answer": "ton"},
        {"question": "What goes up but never comes down?", "answer": "age"},
        {"question": "Which word in the dictionary is spelled incorrectly?", "answer": "incorrectly"}
    ]

    riddle = random.choice(riddles)
    answer = riddle["answer"]

    typewriter(riddle["question"])
    print()

    attempts = 0

    while True:
        guess = input("Your answer: ").lower()

        if guess == answer:
            typewriter("Correct!- The chest opens.")
            print()
            return True

        else:
            health -= 10 # Wrong answer = -10 health
            print(f"Health: {health}")
            health_bar()

            if health <= 0:
                print("You have ran out of health... Game Over.")
                start_menu()
                return False

            attempts += 1
            typewriter("Wrong answer. The chest remains locked.")
            print()

            revealed = answer[:attempts]
            hidden = "_" * (len(answer) - attempts)

            print("Hint:", revealed + hidden)






def movement(): # locations, presents options for the user

    while True:
        if len(visited) == 4:

            if not all(item in inventory for item in required_items):
                typewriter("You have explored everywhere...")
            boat_escape()
            return

        print("Where would you like to explore?")
        if "beach" not in visited:
            print("1. Beach")
        if "forest" not in visited:
            print("2. Forest")
        if "cave" not in visited:
            print("3. Cave")
        if "temple_ruins" not in visited:
            print("4. Temple Ruins")

        response = check2("Please enter your choice: ")

        if response == 1 and "beach" not in visited:
            visited.add("beach")
            beach()

        elif response == 2 and "forest" not in visited:
            visited.add("forest")
            forest()

        elif response == 3 and "cave" not in visited:
            visited.add("cave")
            cave()

        elif response == 4 and "temple_ruins" not in visited:
            visited.add("temple_ruins")
            temple_ruins()

        else:
            typewriter("You have already explored this area.")


# Locations

def beach(): # for the rudder
    typewriter("You choose to explore the beach, look through the wreckage for a rudder to repair your boat.")
    print()
    response = check3("Search for the rudder? Y/N:")

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
                typewriter("You found a hammer!")
                print()
                inventory.append("Hammer")

                response = check3("Make your way back to the rudder. Y/N:")
                if response == "Y" or response == "y":
                    print()
                    typewriter("You made your way back, and broke the rocks with your hammer to get the rudder.")
                    print()
                    inventory.append("Rudder")
                    visited.add("beach")
                    print("Inventory:", inventory)
                    print()
                    movement()

                elif response == "N" or response == "n":
                    movement()





    elif response == "N" or response == "n":
            movement()

def forest(): #for the keel
    typewriter("You chose to explore the forest, look around for useful resources and the keel to help repair your boat.")
    print()
    response = check3("Search for the keel? Y/N: ")
    if response == "Y" or response == "y":
        print()
        typewriter("At the beach the keel is nowhere to be found. You suggest that the wind from the storm has blown the keel deep")
        print()
        typewriter("into the forest.")
        print()
        typewriter("You decide to head into the forest, hoping to find useful resources and the keel.")
        print()
        typewriter("The trees tower above you, blocking out most of the sunlight. You hear strange noises...")
        print()
        response = check3("Continue deeper into the forest? Y/N: ")

        if response == "Y" or response == "y":
            print()
            typewriter("You carefully follow the narrow path.")
            print()
            typewriter("After the while you come across an abandoned campsite.")
            print()
            response = check3("Search the campsite? Y/N: ")

            if response == "Y" or response == "y":
                print()
                typewriter("You search through the campsite and find a locked supply crate.")
                print()
                typewriter("But to open the crate you need to solve a riddle:")
                print()

                result = riddles()

                if result:
                    print()
                    typewriter("The crate opens. Inside, you find a sharp knife and banana's.")
                    print()
                    inventory.append("Knife")
                    inventory.append("Banana's")
                    print("Inventory:", inventory)

                    print()
                    typewriter("As your leaving, you hear rustling in the bushes nearby...")
                    print()

                    response = check3("Investigate the noise? Y/N: ")

                    if response == "Y" or response == "y":
                        print()
                        forest_event()
                        print()
                        typewriter("Using your knife. It runs off, but it drops something...")
                        print()
                        inventory.append("Keel")
                        visited.add("forest")
                        print("Inventory:", inventory)
                        print()
                        movement()

                    elif response == "N" or response == "n":
                        print()
                        typewriter("You decide it's safer not to risk it and leave the forest.")
                        print()
                        movement()

            elif response == "N" or response == "n":
                print()
                typewriter("You ignore the campsite and continue walking until the forest becomes to dark.")
                print()
                typewriter("With no clear path forward, you head back.")
                print()
                movement()

        elif response == "N" or response == "n":
            print("You don't want to get lost in the forest and turn back.")
            print()
            movement()


    elif response == "N" or response == "n":
        movement()


def cave(): #for the sail
    typewriter("As you were searching the beach, you noticed the sail had a huge hole in the middle and was")
    print()
    typewriter("no longer useable.")
    print()
    typewriter("Then you noticed a cave close by... Find items to craft a new sail.")
    print()
    print("Sail Requirements: (Rope),(Sheet)")
    print()

    response = check3("Enter the cave? Y/N:")

    if response == "Y" or response == "y":
        typewriter("You step into the cave, your footsteps and water droplets echoing against the slippery stone.")
        print()
        typewriter("As your eyes adjust to the darkness, you notice another narrow cave entrance.")
        print()

        response = check3("Explore deeper into the cave? Y/N: ")

        if response == "Y" or response == "y":
            print()
            typewriter("You move deeper into the cave, crawling and sliding through narrow pathways and discover a hidden chamber.")
            print()
            typewriter("In the chamber lies an ancient box covered in dust and strange markings.")
            print()

            response = check3("Open the box? Y/N: ")

            if response == "Y" or response == "y":
                print()
                typewriter("The box is locked. To unlock it you need to solve a riddle.")
                print()

                result = riddles()

                if result:
                    print()
                    typewriter("Inside, you find a rope and a torch.")
                    print()
                    inventory.append("Rope")
                    inventory.append("Torch")
                    print("Inventory:", inventory)

                    print()
                    typewriter("As your grabbing the items, you suddenly feel the the ground rumbling and the door behind you slowly closing.")
                    print()
                    response = check3("Run out of the room? Y/N: ")
                    if response == "Y" or response == "y":
                        print()
                        typewriter("As your sprinting out of the room,")
                        cave_event()

                        typewriter("you sprint back towards the entrance, picking up the sheet on your way")
                        print()
                        inventory.append("Sheet")
                        print("Inventory:", inventory)
                        print()

                        response = check3("Craft the Sail?: Y/N:")

                        if response == "Y" or response == "y":
                            if "Rope" in inventory and "Sheet" in inventory:
                                typewriter("Sail crafted.")
                                inventory.append("Sail")
                                visited.add("cave")
                                inventory.remove("Rope")
                                inventory.remove("Sheet")
                                print()
                                print("Inventory:", inventory)

                            else:
                                typewriter("You need Rope and a Sheet to craft the Sail")
                            print()
                            movement()

                        elif response == "N" or response == "n":
                            movement()

                    elif response == "N" or response == "n":
                        print()
                        typewriter("You hesitate, and the rocks pile on you.")
                        print()
                        typewriter("Game Over...")
                        print()
                        start_menu()

            elif response == "N" or response == "n":
                print()
                typewriter("You decided to not risk opening the box and leave the cave.")
                print()
                movement()

        elif response == "N" or response == "n":
            print()
            typewriter("You feel uneasy and decide to leave the cave.")
            print()
            movement()

    elif response == "N" or response == "n":
        print()
        typewriter("You decide it's too dangerous to enter and head back.")
        print()
        movement()


def temple_ruins(): # for the engine part
    typewriter("As you were searching your boat you noticed that a part of the engine was busted,")
    print()
    typewriter("and needed a specific part to fix it.")
    print()
    typewriter("As you were searching around for the part, you noticed a strange building in the distance.")
    print()
    typewriter("When you got closer you saw that it was temple ruins.")
    print()
    typewriter("Explore the ruins to find the missing engine part.")
    print()
    response = check3("Enter? Y/N:")

    if response == "Y" or response == "y":
        typewriter("You step into the temple, your footsteps echoing while you're stepping over vines.")
        print()
        typewriter("As you walk deeper into the temple you stumble across 3 doors.")
        print()
        print("1. Door 1")
        print("2. Door 2")
        print("3. Door 3")
        response = check("Which door do you pick?: ")

        typewriter("When you walk through the door,")

        temple_ruins_event()

        response = check3("Explore deeper? Y/N:")

        if response == "Y" or response == "y":
            typewriter("You move deeper into the temple, dodging and weaving through obstacles and booby traps.")
            print()
            typewriter("Until you discover upon another door.")
            print()
            response = check3("Open the door? Y/N:")

            if response == "Y" or response == "y":
                typewriter("When you open the door you see a large chest in the center of the room.")
                print()
                typewriter("You try to open it but it's locked.")
                print()
                typewriter("And to unlock it you need to answer a riddle.")
                print()
                result = riddles()
                if result:
                    print()
                    typewriter("Inside you find the engine part!")
                    inventory.append("Engine Part")
                    visited.add("temple_ruins")
                    print()
                    print("Inventory:", inventory)
                    print()

                    response = check3("Leave the temple? Y/N:")

                    if response == "Y" or response == "y":
                        print()
                        movement()

                    elif response == "N" or response == "n":
                        typewriter("You decided to keep looking for more resources, and fell into a booby trap!")
                        print("Game Over...")

            elif response == "N" or response == "n":
                typewriter("You decided to not risk it, and left the temple.")
                movement()

        elif response == "N" or response == "n":
            typewriter("You felt uneasy to enter, and left the temple.")
            movement()

    elif response == "N" or response == "n":
        typewriter("You decided it was to dangerous and headed back.")
        movement()




# Random events can affect the users health

def beach_event():
    event = random.randint(1,3)

    if event == 1:
        typewriter("you find water.")
        inventory.append("Water")
        print()
        print("Inventory", inventory)
        typewriter("And right next to it is your tool chest")

    elif event == 2:
        typewriter("you step on sharp glass!")
        global health
        health -= 10
        print()
        health_bar()

    else:
        typewriter("you find your tool chest.")

def forest_event():
    global health

    event = random.randint(1,2)

    if event == 1:
        typewriter("I wild mongoose attacks you!")
        health -= 10
        print()
        health_bar()
        print()


    elif event == 2:
        typewriter("You discover a trapped animal caught in vines.")



def cave_event():
    global health

    event = random.randint(1,3)

    if event == 1:
        typewriter("A small rock hit you in the head!")
        health -= 10
        print()
        health_bar()
        print()

    elif event == 2:
        typewriter("You trip and the rocks blocks the entrance!")
        health -=20
        print()
        health_bar()
        print()

    elif event == 3:
        typewriter("You slide before the rocks could hit you.")


def temple_ruins_event():
    global health

    event = random.randint(1,3)

    if event == 1:
        typewriter(" a poison arrow shoots you in the foot!")
        health -= 20
        print()
        health_bar()
        print()

    elif event == 2:
        typewriter(" a wild boar attacks you!")
        health -= 10
        print()
        health_bar()
        print()

    elif event == 3:
        typewriter(" you find a chest full of apples!")
        inventory.append("Apples")
        print("Inventory", inventory)
        print()

def main_game():
    global visited, inventory, health
    visited = set()
    inventory = []
    health = 100

    game_running = True
    while game_running:

        if len(visited) == 4:
            typewriter("You have explored everywhere...")
            boat_escape()
            game_running = False
            break


def boat_escape():
    print()
    typewriter("Repair your boat and get off this island before it's too late!")
    print()

    response = check3("Return to boat? Y/N:")

    if response == "Y" or response == "y":
        print()

        print("Inventory", inventory)
        print("Required items:", required_items)

        if all(item in inventory for item in required_items):
            print()
            typewriter("You used all the materials to repair the boat...")
            print()
            typewriter("The engine slowly starts.")
            print()
            typewriter("You escape the island safely. You Win!")
            print()
            response = check3("Do you want to play again? Y/N:")
            if response == "Y" or response == "y":
                start_menu()
            elif response == "N" or response == "n":
                exit()

        else:
            typewriter("You don't have everything to fix the boat.")
            print()
            print("You still need:")

            for item in required_items:
                if item not in inventory:
                    print(f"- {item}")

            print()
            typewriter("Explore the island to find all the missing parts.")
            return


#----Start----

start_menu()
print()
movement() #Begin exploration loop

