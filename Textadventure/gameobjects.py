#!/usr/bin/python3

#---------------- Setting of Classes ----------------------------------------------------------
class GameObject:
    class_name=""
    description=""
    objects={}
    location=[]
    status=""

    def __init__(self,name):
        self.name=name
        GameObject.objects[self.class_name]=self              

    def get_description(self):
        return self.class_name + "\n" + self.description

    def get_location(self):
        return self.location

    def get_status(self):
        return self.status


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

class Door(GameObject):
    def __init__(self,name):
        self.class_name = "tuer"
        self.description="Eine schwere hoelzerne Tuer mit Eisenriegel"
        self.location=[2,3]
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
