#!/usr/bin/python3

#---------------- Setting of Classes ----------------------------------------------------------
class GameObject:
    name=""
    class_name=""
    description=""
    objects={}
    location=[]
    status=""
    status2=""
    status3=""
    content=""
    items=[]

    def __init__(self,name):
        self.name=name
        GameObject.objects[self.class_name]=self             
        print(GameObject.objects)

    def get_description(self):
        return self.class_name + "\n" + self.description

    def get_location(self):
        return self.location

    def get_status(self):
        return self.status


class Goblin(GameObject):
    def __init__(self,name,x,y):
        self.class_name = name
        self.description= "Eine grausame Kreatur"
        self.health=3
        self.location=[x,y]
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

class Player(GameObject):
    def __init__(self,name,x,y):
        self.class_name = name
        self.description= "Das bist du"
        self.health=10
        self.items=[]
        self.location=[x,y]
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

class Wizard(GameObject):
    def __init__(self,name,x,y):
        self.class_name = name
        self.description= "Ein grauer weiser Zauberer."
        self.health=2
        self.location=[x,y]
        super().__init__("zauberer")

    @property 
    def description(self):
        if self.health ==2:
            health_line = "Er sieht sehr gebrechlich und vom Leben gezeichnet aus."
            self.health-=1
        elif self.health==1: 
            health_line = "Er bringt unter stoehnen hervor:\n '...mmmhhh? Du.... Du musst es sein... ja so muss es sein ... du bist unserer einzige Hoffnung...ich wuensche dir viel glueck...mmmhhhh....' "
            self.health-=1
            GameObject.objects['spieler'].items.append("zellenschluessel")
            GameObject.objects['spieler'].items.append("weltkarte")
        elif self.health<=0:
            health_line= "Er ist sanft eingeschlafen und aus dem Leben geglitten."
        return self._description + "\n" + health_line

    @description.setter
    def description(self, value):
        self._description = value

class Door(GameObject):
    def __init__(self,name,locked,key,x,y):
        self.name=name
        self.class_name = name
        self.description="Eine schwere hoelzerne Tuer mit Eisenriegel"
        self.location=[x,y]
        self.status="closed"
        self.status2=locked
        self.status3=key
        super().__init__(name)

    @property
    def description(self):
        if self.status=="closed":
            if self.status2=="locked":
                msg="Sie ist abgeschlossen"
            else:
                msg="Sie ist geschlossen"
        elif self.status=="opened":
            msg="Sie ist offen"
        return self._description + "\n" + msg    

    @description.setter
    def description(self,value):
        self._description=value

class Chest(GameObject):
    def __init__(self,name,content,x,y):
        self.class_name = name
        self.description="Eine alte Truhe"
        self.location=[x,y]
        self.status="closed"
        self.content=content
        super().__init__("truhe")

    @property
    def description(self):
        if self.status=="closed":
            msg="Die Truhe ist geschlossen"
        elif (self.status=="opened" and self.content=="dynamit") :
            msg="Die Truhe ist offen, es liegt eine Stange Dynamit darin."
        else :
            msg="Die Truhe ist leer."
        #print(self.status,self.content)
        return self._description + "\n" + msg    

    @description.setter
    def description(self,value):
        self._description=value
