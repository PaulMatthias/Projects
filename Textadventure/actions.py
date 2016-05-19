#!/usr/bin/python3
import gameobjects
import load_level
import maps
#--------------------------------- Here all actions are listed -------------------------------------------------------

def sag(noun):
    return 'Du hast "{}" gesagt'.format(noun)

def hit(noun):
    if noun in gameobjects.GameObject.objects:
        thing=gameobjects.GameObject.objects[noun]
        if type(thing)==gameobjects.Goblin and gameobjects.Player.location == gameobjects.GameObject.objects[noun].location:
            thing.health=thing.health-1
            if thing.health<=0:
                msg= "Du hast den Goblin getoetet"
            else:
                msg= "Du hast den {} getroffen".format(thing.class_name)
        else:
            msg="Hier gibt es keinen {}".format(noun)
    else:
        msg= "Inkorrekte Eingabe"
    return(msg)

def oeffne(noun):
    if noun in load_level.list_of_objects: #gameobjects.GameObject.objects:
        thing=gameobjects.GameObject.objects[noun]
        if type(thing)==gameobjects.Door and load_level.spieler_loc == gameobjects.GameObject.objects[noun].location:
            if thing.status=="opened":
                msg="Tuer ist schon geoffnet"
            elif thing.status2=="locked":
                msg="Tuer ist abgeschlossen"
                if load_level.celldoor_stat3 in load_level.spieler_items:
                    loc=gameobjects.GameObject.objects[noun].location
                    thing.status="opened"
                    thing.status2="opened"
                    load_level.Intro_map_cont[loc[0],loc[1]+1]="nichts"
                    msg="Du hast die Tuer mit {} aufgeschlossen".format(load_level.celldoor_stat3)
            else:
                loc=gameobjects.GameObject.objects[noun].location
                thing.status="opened"
                load_level.Intro_map_cont[loc[0],loc[1]+1]="nichts"
                msg="Du hast die Tuer geoeffnet"
        elif type(thing)==gameobjects.Chest and load_level.spieler_loc == gameobjects.GameObject.objects[noun].location:
            if thing.status=="opened":
                msg="Die Truhe ist schon offen."
            else:
                load_level.truhe_stat="opened"
                msg="Du hast die Truhe geoeffnet."
        else:
            msg= "Hier gibt es keine {}".format(thing.class_name)
    else:
        msg="Inkorrekte Eingabe"
    return(msg)
            

def examine(name):
    if name in load_level.list_of_objects and load_level.spieler_loc == gameobjects.GameObject.objects[name].location:

        return gameobjects.GameObject.objects[name].get_description()
    else:
        return "Hier gibt es keinen {}".format(name)



def move(noun):
    loc=load_level.spieler_loc
    #Sanity check for location    
    #if loc[0]<0 or loc[1]<0 or loc[0]>maps.Intro.map_size[0] or loc[1]>maps.Intro.map_size[1]:
    #    return 'Ausserhalb der Map, Cheater'
    
    #check for map content
    future_location=get_future_location(noun)
    map_content_now= load_level.Intro_map_cont[loc[0],loc[1]]  #maps.Map.get_map_content(maps.Map,loc)
    map_content_future=load_level.Intro_map_cont[future_location[0],future_location[1]]  #maps.Map.get_map_content(maps.Map,future_location)

    if map_content_future=="door_lock" or map_content_future=="door":
        door_status=load_level.celldoor_stat     #gameobjects.GameObject.objects['tuer'].status

    if map_content_future=="chest":
        chest_status=load_level.truhe_stat   #gameobjects.GameObject.objects['truhe'].status

    if map_content_future!="door_lock" or door_status=="open":
        if map_content_future=="wall":
            msg="Dort ist eine Mauer im weg"
        elif noun=="nord":
            load_level.spieler_loc[1]+=1 #gameobjects.Player.location[1]+=1
            msg="Du bist Richtung Norden gegangen\n"
        elif noun=="ost":
            msg="Du bist Richtung Osten gegangen\n"
            load_level.spieler_loc[0]+=1
            #gameobjects.Player.location[0]+=1
        elif noun=="sued":
            msg="Du bist Richtung Sueden gegangen\n"
            load_level.spieler_loc[1]-=1
            #gameobjects.Player.location[1]-=1
        elif noun=="west":
            msg="Du bist Richtung Westen gegangen\n"
            load_level.spieler_loc[0]-=1
            #gameobjects.Player.location[0]-=1
        else:
            msg= "Es gibt keine Richtung {}\n".format(noun)
    else:
        msg=""

    if map_content_future=="nichts":
        msg2 = "Hier befindet sich nur ein leerer Flur"
    elif map_content_future=="goblin":
        description=examine("goblin")
        msg2 = "Hier befindet sich ein {}".format(description)
    elif map_content_future=="zauberer":
        description=examine("zauberer")
        msg2 = "Hier befindet sich ein {}".format(description)
    elif map_content_future=="door_lock" or map_content_future=="door":
        msg2="Dort ist eine Tuer in der Wand, sie ist {}".format(door_status)
    elif map_content_future=="chest":
        msg2="Hier ist eine Truhe, sie ist {}".format(chest_status)
    else:
        msg2=""

    print(future_location)                                         #TODO just for testing Purposes, remove when done
    return(msg + msg2)

def give_location():
    loc=load_level.spieler_loc
    return 'Du bist bei {}'.format(loc)

def stop():
    exit()

def take(noun):
    if noun == load_level.truhe_cont: #gameobjects.Chest.content:
        if load_level.spieler_loc == load_level.truhe_loc: #gameobjects.Player.location == gameobjects.Chest.location:
            if  load_level.truhe_stat=="closed":   #gameobjects.GameObject.objects['truhe'].status=="closed":
                msg="Die Truhe ist noch verschlossen.\n"
            elif load_level.truhe_stat=="opened" and load_level.truhe_cont!="empty":   #gameobjects.GameObject.objects['truhe'].status=="opened" and gameobjects.Chest.content!="empty":
                items=load_level.spieler_items
                items.append(load_level.truhe_cont)
                print(items)
                msg="Du hast {} aus der Truhe genommen".format(load_level.truhe_cont)
                load_level.truhe_cont="empty"
            else:
                msg="Die Truhe ist leer."
        else:
            msg="Hier gibt es kein {}".format(noun)
    else:
        msg="Du kannst das hier nicht nehmen."
    return msg          
            
def item_list():
    return load_level.spieler_items #gameobjects.GameObject.objects['spieler'].items

def helpme():
    msg='\n'
    msg+="Die wichigsten Befehle:\n"
    msg+="'sag #Eingabe': sage irgendetwas\n"
    msg+="'gehe nord/ost/sued/west': bewege dich auf der Karte\n"
    msg+="'oeffne #Eingabe': oeffnet Gegenstaende\n"
    msg+="'schlage #Eingabe': Kampf mit Gegner\n"
    msg+="'untersuche #Eingabe': untersucht Gegenstand oder Person\n"
    msg+="'position': Gibt deine aktuelle Position in Form von Koordinaten wieder\n"
    msg+="'exit': Verlaesst das Spiel"
    return msg

verb_dict= {
        "sag":sag,
        "untersuche":examine,
        "schlage":hit,
        "gehe" :move,
        "position":give_location,
        "oeffne":oeffne,
        "nimm":take,
        "items":item_list,
        "Exit":stop,
        "Hilfe":helpme,
}

def get_future_location(noun):
    future_location=[load_level.spieler_loc[0],load_level.spieler_loc[1]]
    if noun=="nord":
        future_location[1]=load_level.spieler_loc[1]+1
    elif noun=="ost":
        future_location[0]=load_level.spieler_loc[0]+1
    elif noun=="sued":
        future_location[1]=load_level.spieler_loc[1]-1
    elif noun=="west":
        future_location[0]=load_level.spieler_loc[0]-1
    else:
        msg= "Es gibt keine Richtung {}".format(noun)
    return future_location

