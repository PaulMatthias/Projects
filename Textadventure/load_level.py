#!/usr/bin/python3

import maps
import gameobjects

#maps.Map.map_content=maps.Intro.set_map_content(maps.Intro)    

Intro_map=maps.Intro.set_map_content(maps.Intro)    

Intro_map=maps.Verlies("Verlies", 5,7)
Intro_map_name=Intro_map.name
Intro_map_cont_init,Intro_map_cont=Intro_map.set_map_content()
zauberer=gameobjects.Wizard("zauberer",2,1)
wizard_name=zauberer.name
wizard_loc=zauberer.location
wizard_des=zauberer.description
spieler=gameobjects.Player("spieler",1,1)
spieler_name=spieler.name
spieler_loc=spieler.location
spieler_des=spieler.description
spieler_items=spieler.items
truhe=gameobjects.Chest("truhe","dynamit",4,4)
truhe_name=truhe.name
truhe_loc=truhe.location
truhe_des=truhe.description
truhe_cont=truhe.content
truhe_stat=truhe.status
celldoor=gameobjects.Door("tuer","locked","zellenschluessel",2,2)
celldoor_name=celldoor.name
celldoor_loc=celldoor.location
celldoor_des=celldoor.description
celldoor_cont=celldoor.content
celldoor_stat=celldoor.status
celldoor_stat2=celldoor.status2
celldoor_stat3=celldoor.status3
celldoor1=gameobjects.Door("tuer1","locked","",2,6)
celldoor1_name=celldoor1.name
celldoor1_loc=celldoor1.location
celldoor1_des=celldoor1.description
celldoor1_cont=celldoor1.content
celldoor1_stat=celldoor1.status
celldoor1_stat2=celldoor1.status2
celldoor1_stat3=celldoor1.status3

list_of_objects={Intro_map_name, wizard_name, spieler_name, truhe_name, celldoor_name}

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
        maps.Map.map_content=maps.Intro.set_map_content(maps.Intro)    
        zauberer=gameobjects.Wizard("Opi",2,1)
        wizard_loc=zauberer.location
        wizard_des=zauberer.description
        spieler=gameobjects.Player("Held",1,1)
        spieler_loc=spieler.location
        spieler_des=spieler.description
        truhe=gameobjects.Chest("truhe1","dynamit",4,4)
        truhe_loc=truhe.location
        truhe_des=truhe.description
        truhe_cont=truhe.content
        truhe_stat=truhe.status
        celldoor=gameobjects.Door("tuer1","locked","Zellenschluessel",2,2)
        celldoor_loc=celldoor.location
        celldoor_des=celldoor.description
        celldoor_cont=celldoor.content
        celldoor_stat=celldoor.status
        celldoor_stat2=celldoor.status2
        celldoor_stat3=celldoor.status3
        return maps.Map.map_content,spieler,zauberer,truhe,celldoor
    else:
        print('Falsches Level\n')

def reset():
    for thing in gameobjects.GameObject.objects:
        gameobjects.GameObject.objects[thing].location=[]
