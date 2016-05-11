#!/usr/bin/python3

import maps
import gameobjects

def load_level(map_name):
    if map_name=="Intro":
        reset()
        maps.Map.map_content=maps.Intro.set_map_content(maps.Intro)
        gameobjects.Goblin.location=[2,2]
        gameobjects.Player.location=[1,1]
        gameobjects.Door.location=[2,3]
        return maps.Map.map_content
    elif map_name=="Verlies":
        #reset()
        maps.Map.map_content=maps.Verlies.set_map_content(maps.Verlies)
        gameobjects.Player.location=[1,1]
        gameobjects.Wizard.location=[2,1]
        gameobjects.Door.location=[2,2]
       # gameobjects.Door.location+=[2,6] TODO think abbout multiple door locations
        gameobjects.Chest.location=[4,4]
        gameobjects.Chest.content="dynamit"
        return maps.Map.map_content
    else:
        print('Falsches Level\n')

def reset():
    for thing in gameobjects.GameObject.objects:
        gameobjects.GameObject.objects[thing].location=[]
