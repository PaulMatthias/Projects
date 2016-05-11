#!/usr/bin/python3
import gameobjects
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
    if noun in gameobjects.GameObject.objects:
        thing=gameobjects.GameObject.objects[noun]
        if type(thing)==gameobjects.Door and gameobjects.Player.location == gameobjects.GameObject.objects[noun].location:
            if thing.status=="opened":
                msg="Tuer ist schon geoffnet"
            else:
                loc=gameobjects.GameObject.objects[noun].location
                thing.status="opened"
                maps.Map.map_content[0][loc[0],loc[1]+1]="nichts"
                msg="Du hast die Tuer geoeffnet"
        elif type(thing)==gameobjects.Chest and gameobjects.Player.location == gameobjects.GameObject.objects[noun].location:
            if thing.status=="opened":
                msg="Die Truhe ist schon offen."
            else:
                thing.status="opened"
                msg="Du hast die Truhe geoeffnet."
        else:
            msg= "Hier gibt es keine {}".format(thing.class_name)
    else:
        msg="Inkorrekte Eingabe"
    return(msg)
            

def examine(noun):
    if noun in gameobjects.GameObject.objects and gameobjects.Player.location == gameobjects.GameObject.objects[noun].location:

        return gameobjects.GameObject.objects[noun].get_description()
    else:
        return "Hier gibt es keinen {}".format(noun)



def move(noun):
    loc=gameobjects.Player.location
    #Sanity check for location    
    #if loc[0]<0 or loc[1]<0 or loc[0]>maps.Intro.map_size[0] or loc[1]>maps.Intro.map_size[1]:
    #    return 'Ausserhalb der Map, Cheater'
    
    #check for map content
    future_location=get_future_location(noun)
    map_content_now=maps.Map.get_map_content(maps.Map,loc)
    map_content_future=maps.Map.get_map_content(maps.Map,future_location)

    if map_content_future=="door_lock" or map_content_future=="door":
        door_status=gameobjects.GameObject.objects['tuer'].status

    if map_content_future=="chest":
        chest_status=gameobjects.GameObject.objects['truhe'].status

    if map_content_future!="door_lock" or door_status=="open":
        if map_content_future=="wall":
            msg="Dort ist eine Mauer im weg"
        elif noun=="nord":
            gameobjects.Player.location[1]+=1
            msg="Du bist Richtung Norden gegangen\n"
        elif noun=="ost":
            msg="Du bist Richtung Osten gegangen\n"
            gameobjects.Player.location[0]+=1
        elif noun=="sued":
            msg="Du bist Richtung Sueden gegangen\n"
            gameobjects.Player.location[1]-=1
        elif noun=="west":
            msg="Du bist Richtung Westen gegangen\n"
            gameobjects.Player.location[0]-=1
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
    loc=gameobjects.Player.location
    return 'Du bist bei {}'.format(loc)

def stop():
    exit()

def take(noun):
    if noun == gameobjects.Chest.content:
        if gameobjects.Player.location == gameobjects.Chest.location:
            if gameobjects.GameObject.objects['truhe'].status=="closed":
                msg="Die Truhe ist noch verschlossen.\n"
            elif gameobjects.GameObject.objects['truhe'].status=="opened" and gameobjects.Chest.content!="empty":
                items=gameobjects.GameObject.objects['spieler'].items
                items.append(gameobjects.Chest.content)
                print(items)
                msg="Du hast {} aus der Truhe genommen".format(gameobjects.Chest.content)
                gameobjects.Chest.content="empty"
            else:
                msg="Die Truhe ist leer."
        else:
            msg="Hier gibt es kein {}".format(noun)
    else:
        msg="Du kannst das hier nicht nehmen."
    #print(gameobjects.GameObject.objects['truhe'].status)
    return msg          
            
def item_list():
    return gameobjects.GameObject.objects['spieler'].items

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
}

def get_future_location(noun):
    future_location=[gameobjects.Player.location[0],gameobjects.Player.location[1]]
    if noun=="nord":
        future_location[1]=gameobjects.Player.location[1]+1
    elif noun=="ost":
        future_location[0]=gameobjects.Player.location[0]+1
    elif noun=="sued":
        future_location[1]=gameobjects.Player.location[1]-1
    elif noun=="west":
        future_location[0]=gameobjects.Player.location[0]-1
    else:
        msg= "Es gibt keine Richtung {}".format(noun)
    return future_location

