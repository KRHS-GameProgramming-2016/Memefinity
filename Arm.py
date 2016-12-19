import pygame, sys, math
from Player import *

class Arm(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.runRight = pygame.image.load("rsc/ball/PlayerArm.png")
        self.runLeft = pygame.image.load("rsc/ball/PlayerArmLeft.png")
        self.restRight = [pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArm.png"), [100,100])]
        self.restLeft = [pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArmLeft.png"), [100,100])]
        self.images = self.restRight
        self.state = "rest right"
        self.prevState = "rest right"
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
    
    def update(self):
        self.rect.center = [self.player.rect.x+46, 
                            self.player.rect.y+38]

        if self.prevState != self.state:
            self.prevState = self.state
            if self.player.state == "run right":
                self.images = self.runRight
                self.rect.center = [self.player.rect.x+37, 
                self.player.rect.y+38]
            if self.player.state == "run left":
                self.images = self.runLeft
                self.rect.center = [self.player.rect.x+51, 
                self.player.rect.y+38]
            if self.player.state == "rest right":
                self.images = self.restRight
            if self.player.state == "rest left":
                self.images = self.restLeft
