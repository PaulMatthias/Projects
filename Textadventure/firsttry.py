#!/usr/bin/python3


#This is the first try of developping a text adventure game based on python3 
# This file will contain the description of the charakter,, one enemy class, a simple map design, some interactive items, a fight scene and the overall hud+movement system


#---------------- Setting of Classes ----------------------------------------------------------
class GameObject:
    class_name=""
    description=""
    objects={}
    location=[]

    def __init__(self,name):
        self.name=name
        GameObject.objects[self.class_name]=self

    def get_description(self):
        return self.class_name + "\n" + self.description

    def get_location(self):
        return self.location

class Player(GameObject):
    def __init__(self,name):
        self.class_name = "Spieler"
        self.description= "Das bist du"
        self.health=10
        self.location=[2,1]
        super().__init__(name)

    @property 
    def description(self):
        if self.health>=3:
            return self._description
        elif self.health==2:
            health_line = "Du bist am Knie verwundet"
        elif self.health ==1:
            health_line = "Dein linker Arm ist abgefallen"
        elif self.health<=0:
            health_line= "Du bist tot"
        return self._description + "\n" + health_line

    @description.setter
    def description(self, value):
        self._description = value



class Goblin(GameObject):
    def __init__(self,name):
        self.class_name = "goblin"
        self.description= "Eine grausame Kreatur"
        self.health=3
        self.location=[2,3]
        super().__init__(name)


    @property 
    def description(self):
        if self.health>=3:
            return self._description
        elif self.health==2:
            health_line = "Er ist am Knie verwundet"
        elif self.health ==1:
            health_line = "Sein linker Arm ist abgefallen"
        elif self.health<=0:
            health_line= "Er ist tot"
        return self._description + "\n" + health_line

    @description.setter
    def description(self, value):
        self._description = value

#--------------------------------- Map initialisation and boundary conditions----------------------------------------------

class Map:
    map_size=[]
    map_name=""
    levels={}

    def __init__(self,name):
        self.name=name
        Map.levels[self.map_name]=self

class Intro(Map):
    def __init__(self,name):
        self.map_name="Intro Karte"
        self.map_size=[2,2]
        super().__init__(name)
    

#--------------------------------- Here all actions are listed -------------------------------------------------------

def sag(noun):
    return 'Du hast "{}" gesagt'.format(noun)

def hit(noun):
    if noun in GameObject.objects:
        thing=GameObject.objects[noun]
        if type(thing)==Goblin:
            thing.health=thing.health-1
            if thing.health<=0:
                msg= "Du hast den Goblin getoetet"
            else:
                msg= "Du hast den {} getroffen".format(thing.class_name)
        else:
            msg="Hier gibt es keinen {}".format(noun)
    else:
        msg= "Was hast du gesagt?"
    return(msg)

def examine(noun):
    if noun in GameObject.objects and Player.location == GameObject.objects[noun].location:
        return GameObject.objects[noun].get_description()
    else:
        return "Hier gibt es keinen {}".format(noun)

def move(noun):
    loc=Player.location
    #Sanity check for location    
    if loc[0]<0 or loc[1]<0 or loc[0]>Intro.map_size[0] or loc[1]>Intro.map_size[1]:
        return 'Ausserhalb der Map, Cheater'

    if noun=="nord":
        msg="Du bist nach Norden gegangen"
        Player.location[1]+=1
    elif noun=="ost":
        msg="Du bist nach Osten gegangen"
        Player.location[0]+=1
    elif noun=="sued":
        msg="Du bist nach Sueden gegangen"
        Player.location[1]-=1
    elif noun=="west":
        msg="Du bist nach Westen gegangen"
        Player.location[0]-=1
    else:
        msg= "Es gibt keine Richtung {}".format(noun)
    return(msg)

def give_location():
    loc=Player.location
    return 'Du bist bei {}'.format(loc)

verb_dict= {
        "sag":sag,
        "untersuche":examine,
        "schlag":hit,
        "gehe" :move,
        "position":give_location,
}

goblin=Goblin("Knarf")


#-----------------  Get input and evaluate what to do -------------------------------------------------
def get_input():
    command=input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unbekannter Befehl {}". format(verb_word))
        return

    if len(command) >=2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())




#------------------------Initialisiere Spiel-------------------------------------------------------------------
Player.location=[2,1]
Intro.map_size=[2,2]


while True:
    get_input()
