#10/03/2026

#Library Imports

import time, sys
import random

#----Variables----

hunger = 100

#----Functions----

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def intro():
    print("------------------------------")
    print("ISLAND ESCAPE - Text Adventure")
    print("------------------------------")

    typewriter("You wake to the sound of waves crashing against the shore.")
    print()
    typewriter("You slowly open your eyes. The last thing you remember is sailing on your boat when an extreme storm")
    print()
    typewriter("appeared out of nowhere.")
    print()
    typewriter("You find yourself lying on the warm sand of a strange island surrounded by a thick jungle and")
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

#----Start----

intro()