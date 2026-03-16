#Libraries
import random
import time

#Variables
wild_pokemon = [
    {"Name":"Charizard","Type":"Fire","Level":random.randint(1, 6), "Health":random.randint(15, 25),"Attack":["Ember",random.randrange(3,6), "Flamethrower",random.randrange(8,25)]},
    {"Name":"Venasuar","Type":"Grass","Level":random.randint(1, 6), "Health":random.randint(18, 22),"Attack":["Ember",random.randrange(3,6), "Flamethrower",random.randrange(8,25)]},
    {"Name":"Blastoise","Type":"Water","Level":random.randint(1, 6), "Health":random.randint(12, 30),"Attack":["Ember",random.randrange(3,6), "Flamethrower",random.randrange(8,25)]},
    {"Name":"Mew","Type":"Normal","Level":random.randint(1, 6), "Health":random.randint(14, 28),"Attack":["Ember",random.randrange(3,6), "Flamethrower",random.randrange(8,25)]},
    {"Name":"Snorlax","Type":"Normal","Level":random.randint(1, 6), "Health":random.randint(8, 32),"Attack":["Ember",random.randrange(3,6), "Flamethrower",random.randrange(8,25)]},
    {"Name":"Eevee","Type":"Normal","Level":random.randint(1, 6), "Health":random.randint(16, 28),"Attack":["Ember",random.randrange(3,6), "Flamethrower",random.randrange(8,25)]},
    {"Name":"Pikachu","Type":"Normal","Level":random.randint(1, 6), "Health": random.randint(16, 28),"Attack": ["Ember", random.randrange(3, 6), "Flamethrower", random.randrange(8, 25)]}
]
own_pokemon = [{"Name":"Pidgy", "Type":"Flying", "Level":3, "Health":20,"Attack":["Flap",random.randint]}]
#Functions
def overworld_timer():
    timer = random.randint(1,5)
    print(timer)
    time.sleep(timer)
    print("Battle Begins")
    battle()

def battle():
    x=random.randint(0, len(wild_pokemon)-1)
    enemy_pokemon = wild_pokemon[x]
    player_pokemon = own_pokemon[0]
    player_pokemon_hp = player_pokemon["Health"]
    print("Player pokemon:",player_pokemon["Name"])
    print("Player pokemon HP:",player_pokemon_hp)
    print("A wild",enemy_pokemon["Name"], "appeared")
    print("It's a",enemy_pokemon["Type"], "type Pokemon")
    print("It's level",enemy_pokemon["Level"], "Level")
    print("It has",enemy_pokemon["Health"], "Health")

    while True:

        enemy_attack_randomiser = random.randrange(0,3,2)
        print("Random number for attack", enemy_attack_randomiser)
        print(enemy_pokemon["Name"], "attacks with", enemy_pokemon["Attack"][enemy_attack_randomiser], "for",
                enemy_pokemon["Attack"][enemy_attack_randomiser +1], "damage")
        player_pokemon_hp = player_pokemon_hp - enemy_pokemon["Attack"][enemy_attack_randomiser +1]
        print(player_pokemon["Name"], "has", player_pokemon_hp, "health")

        overworld_timer()
battle()