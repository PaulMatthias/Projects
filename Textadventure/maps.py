#!/usr/bin/python3

#--------------------------------- Map initialisation and boundary conditions----------------------------------------------

class Map:
    map_size=[]
    map_name=""
    map_content_init={}
    map_content={}
    levels={}

    def __init__(self,name):
        self.name=name
        Map.levels[self.map_name]=self


    def get_map_content(self,location):
        return self.map_content[location[0],location[1]]

class Intro(Map):
    def __init__(self,name):
        self.map_name="intro"
        self.map_size=[5,5]
        super().__init__("intro")
    
    def fill_map_content(self):
        #set walls
        for i in range (0,5):
            for j in range (0,5):
                if i==0 or i==4 or j==0 or j==4 or (i%2==0 and j%2==0):
                    self.map_content_init[i,j]="wall"
                else:
                    self.map_content_init[i,j]="nichts"
        #set enemies
        self.map_content_init[2,2]="goblin"
        #set doors
        self.map_content_init[2,3]="door"
        self.map_content_init[2,4]="door_lock"
       # content=self.map_content[location[0],location[1]]
        return self.map_content_init

    def set_map_content(self):
        self.map_content_init=self.fill_map_content(self)
        self.map_content=self.map_content_init
        return self.map_content_init, self.map_content

class Verlies(Map):

    def __init__(self,name):
        self.map_name="verlies"
        self.map_size=[5,7]
        super().__init__("verlies")
    
    def fill_map_content(self,location):
        #set corridors
        for i in range (0,5):
            for j in range (0,7):
                if (j==2 and i>0) or (j==1 and i>0 and i!=3 and i!=5 and i!=7) or ((j==3 or j==4) and (i==4 or i==5)):
                    self.map_content[i,j]="nichts"
                else:
                    self.map_content[i,j]="wall"
        #set NPC
        self.map_content[2,3]="zauberer"
        #set doors
        self.map_content[2,3]="door"
        self.map_content[1,6]="door"
        content=self.map_content[location[0],location[1]]
        return content



