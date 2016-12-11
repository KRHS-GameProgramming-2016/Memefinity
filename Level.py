import pygame, sys, math, random
from Wall import *
from Meme import *
from Player import *
class Level():
    def __init__(self, levelNumber, size, tileSize=50):
        self.tileSize = tileSize
        self.size = size
        self.width = size[0]
        self.height = size[1]
        
        self.loadLevel(levelNumber)
        self.world_shift = 0
        
    def shiftWorld(self, groups, amount):
        self.world_shift += amount
        for group in groups:
            for item in group.sprites():
                item.shiftX(amount)
                
    def unloadLevel(self, groups): 
        for group in groups:
            group.empty()
               
    def loadLevel(self, levelNumber):       
        f = open("rsc/levels/level"+str(levelNumber)+".lvl", 'r')
        lines = f.readlines()
        f.close()
        
        """
        print lines
        print "________________________"
        
        for line in lines:
            print line
        print "________________________"
        """
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    Wall([x*self.tileSize + self.tileSize/2,
                         y*self.tileSize + self.tileSize/2],
                         self.tileSize)
                         
                if c == 'P':
                    PlayerMeme(self.size, 7,
                                    [x*self.tileSize + self.tileSize/2,
                                     y*self.tileSize + self.tileSize/2])
#                    Arm(size, player)
                
                if c == 'm':
                    Meme(self.size, 1, 
                        [random.randint(7, 10), random.randint(1, 10)],
                        [x*self.tileSize + self.tileSize/2,
                         y*self.tileSize + self.tileSize/2],
                        random.randint(20, 100))
				
                if c == 'Q':
                    Wall_5x5([x*self.tileSize + self.tileSize/2,
                        y*self.tileSize + self.tileSize/2],
                        self.tileSize)

                                                

        
#Level("level1.lvl")
            
