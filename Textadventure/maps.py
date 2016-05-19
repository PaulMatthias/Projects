#!/usr/bin/python3

#--------------------------------- Map initialisation and boundary conditions----------------------------------------------

class Map:
    map_size=[]
    map_name=""
    map_content_init={}
    map_content=()
    levels={}

    def __init__(self,name):
        self.name=name
        Map.levels[self.map_name]=self

    def get_map_content(self,location):
        return self.map_content[0][location[0],location[1]]

class Intro(Map):
    def __init__(self,name,x,y):
        self.map_name=name
        self.map_size=[x,y]
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
        #set doors and objects
        self.map_content_init[2,3]="door"
        self.map_content_init[2,4]="door_lock"
        return self.map_content_init

    def set_map_content(self):
        self.map_content_init=self.fill_map_content(self)
        self.map_content=self.map_content_init
        return self.map_content_init, self.map_content

class Verlies(Map):

    def __init__(self,name,x,y):
        self.map_name=name
        self.map_size=[x,y]
        super().__init__("verlies")

    
    def fill_map_content(self):
        #set corridors
        for i in range (0,6):
            for j in range (0,8):
                if i==1 and (j==1 or j==2):       # Zelle
                    self.map_content_init[i,j]="nichts"
                elif i==2 and j>0:                  #floor
                    self.map_content_init[i,j]="nichts"
                elif i>2 and i<5 and j>3 and j<6:       #chamber with chest
                    self.map_content_init[i,j]="nichts"
                elif j==0 or i==5 or i==0 or j==7:      #left and right and bot and top wall
                    self.map_content_init[i,j]="wall"
                else:                                   #fill rest with walls
                    self.map_content_init[i,j]="wall"
        #set NPC
        self.map_content_init[2,1]="zauberer"
        #set doors and objects
        self.map_content_init[2,2]="door"
        self.map_content_init[2,3]="door_lock"
        self.map_content_init[2,6]="door"
        self.map_content_init[1,6]="door_lock"
        self.map_content_init[4,4]="chest"
        #set exit to other levels
        self.map_content_init[2,7]="world"
        
       # for i in range (0,6):
       #     for j in range (0,8):
       #         print(i,j,self.map_content_init[i,j])
        return self.map_content_init

    def set_map_content(self):
        self.map_content_init=self.fill_map_content()
        self.map_content=self.map_content_init

        return self.map_content_init, self.map_content


