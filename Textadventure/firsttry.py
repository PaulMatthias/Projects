#!/usr/bin/python3

import actions
import maps
import gameobjects



#This is the first try of developping a text adventure game based on python3 
# This file will contain the description of the charakter,, one enemy class, a simple map design, some interactive items, a fight scene and the overall hud+movement system

#Initialisiere alle wichtigen GameObjects
goblin=gameobjects.Goblin("Knarf")
spieler=gameobjects.Player("Held")
tuer=gameobjects.Door("tuer1")


#Initialisiere alle Karten
intro=maps.Intro("default")
verlies=maps.Verlies("Verlies")

#Initialisiere Maps
intro_map_content=maps.Intro.set_map_content(maps.Intro)
print(maps.Intro.get_map_content(maps.Intro,(2,4)))


#-----------------  Get input and evaluate what to do -------------------------------------------------
def get_input():
    command=input(": ").split()
    verb_word = command[0]
    if verb_word in actions.verb_dict:
        verb = actions.verb_dict[verb_word]
    else:
        print("Unbekannter Befehl {}". format(verb_word))
        return

    if len(command) >=2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())


#------------------------Initialisiere Spiel-------------------------------------------------------------------
gameobjects.Player.location=[1,3]

#starting up Intro Level


while True:
    get_input()
