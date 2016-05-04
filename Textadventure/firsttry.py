#!/usr/bin/python3


#This is the first try of developping a text adventure game based on python3 
# This file will contain the description of the charakter,, one enemy class, a simple map design, some interactive items, a fight scene and the overall hud+movement system


#---------------- Setting of Classes ----------------------------------------------------------
class GameObject:
    class_name=""
    description=""
    objects={}
    location=[]
    status=""

    def __init__(self,name):
        self.name=name
        GameObject.objects[self.class_name]=self              #TODO fix that nothing except goblin appears in in GameObject.objects

    def get_description(self):
        return self.class_name + "\n" + self.description

    def get_location(self):
        return self.location

    def get_status(self):
        return self.status

class Player(GameObject):
    def __init__(self,name):
        self.class_name = "spieler"
        self.description= "Das bist du"
        self.health=10
        self.location=[2,1]
        super().__init__("spieler")

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
        super().__init__("goblin")

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

class Door(GameObject):
    def __init__(self,name):
        self.class_name = "tuer"
        self.description="Eine schwere hoelzerne Tuer mit Eisenriegel"
        self.location=[2,4]
        self.status="closed"
        super().__init__("tuer")

    @property
    def description(self):
        if self.status=="closed":
            msg="Sie ist geschlossen"
        elif self.status=="opened":
            msg="Sie ist offen"
        return self._description + "\n" + msg    

    @description.setter
    def description(self,value):
        self._description=value

#--------------------------------- Map initialisation and boundary conditions----------------------------------------------

class Map:
    map_size=[]
    map_name=""
    map_content={}
    levels={}

    def __init__(self,name):
        self.name=name
        Map.levels[self.map_name]=self

    def get_map_content(self,location):
        return self.fill_map_content(self,location)

class Intro(Map):
    def __init__(self,name):
        self.map_name="Intro Karte"
        self.map_size=[5,5]
        super().__init__(name)
    
    def fill_map_content(self,location):
        #set walls
        for i in range (0,5):
            for j in range (0,5):
                if i==0 or i==4 or j==0 or j==4 or (i%2==0 and j%2==0):
                    self.map_content[i,j]="wall"
                else:
                    self.map_content[i,j]="nichts"
        #set enemies
        self.map_content[2,3]="goblin"
        #set doors
        self.map_content[2,4]="door"
        content=self.map_content[location[0],location[1]]
        return content


    


#--------------------------------- Here all actions are listed -------------------------------------------------------

def sag(noun):
    return 'Du hast "{}" gesagt'.format(noun)

def hit(noun):
    if noun in GameObject.objects:
        thing=GameObject.objects[noun]
        if type(thing)==Goblin and Player.location == GameObject.objects[noun].location:
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
    print(GameObject.objects)
    if noun in GameObject.objects:
        thing=GameObject.objects[noun]
        if type(thing)==Door: #and Player.location == GameObject.objects[noun].location:
            if thing.status=="opened":
                msg="Tuer ist schon geoffnet"
            else:
                thing.status="opened"
                Intro.map_content[2,4]="empty"
                msg="Du hast die Tuer geoeffnet"
        else:
            msg= "Hier gibt es keine {}".format(thing.class_name)
    else:
        msg="Inkorrekte Eingabe"
    return(msg)
            

def examine(noun):
    if noun in GameObject.objects and Player.location == GameObject.objects[noun].location:
        return GameObject.objects[noun].get_description()
    else:
        return "Hier gibt es keinen {}".format(noun)

def move(noun):
    loc=Player.location
    #Sanity check for location    
    #if loc[0]<0 or loc[1]<0 or loc[0]>Intro.map_size[0] or loc[1]>Intro.map_size[1]:
    #    return 'Ausserhalb der Map, Cheater'
    
    #check for map content
    future_location=get_future_location(noun)
    map_content=Intro.get_map_content(Intro,future_location)
    if map_content=="wall":
        msg="Dort ist eine Mauer im weg"
    elif map_content=="door":
        msg="Dort ist eine Tuer in der Wand"
    elif noun=="nord":
        Player.location[1]+=1
        msg="Du bist Richtung Norden gegangen\n"
    elif noun=="ost":
        msg="Du bist Richtung Osten gegangen\n"
        Player.location[0]+=1
    elif noun=="sued":
        msg="Du bist Richtung Sueden gegangen\n"
        Player.location[1]-=1
    elif noun=="west":
        msg="Du bist Richtung Westen gegangen\n"
        Player.location[0]-=1
    else:
        msg= "Es gibt keine Richtung {}".format(noun)

    if map_content=="nichts":
        msg2 = "Hier befindet sich nur ein leerer Flur"
    elif map_content=="goblin":
        description=examine("goblin")
        msg2 = "Hier befindet sich ein {}".format(description)
    else:
        msg2=""

    print(future_location)                                                  #TODO just for testing Purposes, remove when done
    return(msg+msg2)

def give_location():
    loc=Player.location
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
    future_location=[Player.location[0],Player.location[1]]
    if noun=="nord":
        future_location[1]=Player.location[1]+1
    elif noun=="ost":
        future_location[0]=Player.location[0]+1
    elif noun=="sued":
        future_location[1]=Player.location[1]-1
    elif noun=="west":
        future_location[0]=Player.location[0]-1
    else:
        msg= "Es gibt keine Richtung {}".format(noun)
    return future_location


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
Player.location=[1,1]

#starting up Intro Level


while True:
    get_input()
