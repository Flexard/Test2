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
    typewriter("Your plane crashes, you are stranded on an island with no food, water, and resources")
    print()
    typewriter("")
    print()
    typewriter("It's 7pm, your goal is to make it to the escape helicopter before sundown, Good Luck you will need it")
    print()
    typewriter("Find Clues, Solve Riddles, and Collect Resources to help you navigate and progress through the game")


#----Start----

print("------------------------------")
print("ISLAND ESCAPE - Text Adventure")
print("------------------------------")

intro()