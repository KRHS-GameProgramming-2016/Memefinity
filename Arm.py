import pygame, sys, math
from Player import *

class Arm(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.runRight = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArm.png"), [100,100])
        self.runLeft = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArmLeft.png"), [100,100])
        self.restRight = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArm.png"), [100,100])
        self.restLeft = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArmLeft.png"), [100,100])
        self.baseImage = self.restRight
        self.image = self.baseImage
        self.state = "rest right"
        self.prevState = "rest right"
        self.offset = [43,36]
        self.rect = self.image.get_rect()
        self.angle =0
    
    def aim(self, mousePos):           #https://github.com/scscorley/jellitubby-attack/blob/master/Vacuum.py
        """rotate an image while keeping its center and size"""
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        self.angle = -self.angle
        
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
    
    def addOffsets(self):
        print self.rect.center,
        self.rect.center = [self.player.rect.x+self.offset[0], 
                            self.player.rect.y+self.offset[1]]
        print self.offset,  self.rect.center
    
    def update(self):
        self.state = self.player.state
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "run right":
                self.baseImage = self.runRight
                self.offset = [36,36]
            if self.state == "run left":
                self.baseImage = self.runLeft
                self.offset = [60,36]
            if self.state == "rest right":
                self.baseImage = self.restRight
                self.offset = [43,36]
            if self.state == "rest left":
                self.baseImage = self.restLeft
                self.offset = [58,36]
            self.image = self.baseImage
        self.addOffsets()
       
