import pygame, sys, math
from Arm import *

class GunPickup(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.kind = kind 
        if self.kind == "AK47": 
            self.image = pygame.image.load("rsc/ball/bullet.png")
        elif self.kind == "pistol": 
            self.image = pygame.image.load("rsc/ball/bullet.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        #arm.gun = self.kind
        
    def shiftX(self, amount):
        self.rect.x += amount 
        



