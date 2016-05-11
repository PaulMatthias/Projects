#!/usr/bin/python3
import menue
import load_level

import actions
import maps
import gameobjects

#Mainfile for starting the game

#Initialisiere alle wichtigen GameObjects
goblin=gameobjects.Goblin("Knarf")
zauberer=gameobjects.Wizard("Opi")
spieler=gameobjects.Player("Held")
tuer=gameobjects.Door("tuer1")
truhe=gameobjects.Chest("truhe1")


#Initialisiere alle Karten
intro=maps.Intro("default")
verlies=maps.Verlies("Verlies")

#Initialisiere Maps
maps.Map.map_content=load_level.load_level('Verlies')

#------------------------Initialisiere Spiel-------------------------------------------------------------------
#starting up Intro Level

#starting menue
menue.start_menue()

