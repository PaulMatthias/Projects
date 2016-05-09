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
                thing.status="opened"
                maps.Intro.map_content[2,4]="empty"
                msg="Du hast die Tuer geoeffnet"
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
    map_content_now=maps.Intro.get_map_content(maps.Intro,loc)
    map_content_future=maps.Intro.get_map_content(maps.Intro,future_location)

    if map_content_future=="door_lock" or map_content_future=="door":
        door_status=gameobjects.GameObject.objects['tuer'].status

    print(map_content_future)


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
            msg= "Es gibt keine Richtung {}".format(noun)
    else:
        msg=""

    if map_content_future=="nichts":
        msg2 = "Hier befindet sich nur ein leerer Flur"
    elif map_content_future=="goblin":
        description=examine("goblin")
        msg2 = "Hier befindet sich ein {}".format(description)
    elif map_content_future=="door_lock" or map_content_future=="door":
        msg2="Dort ist eine Tuer in der Wand, sie ist {}".format(door_status)
    else:
        msg2=""

    print(future_location)                                                  #TODO just for testing Purposes, remove when done
    return(msg+msg2)

def give_location():
    loc=gameobjects.Player.location
    return 'Du bist bei {}'.format(loc)

verb_dict= {
        "sag":sag,
        "untersuche":examine,
        "schlage":hit,
        "gehe" :move,
        "position":give_location,
        "oeffne":oeffne,
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

