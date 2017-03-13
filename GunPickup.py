import pygame, sys, math
from Arm import *

class GunPickup(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.kind = kind 
        if self.kind == "health": 
            self.image = pygame.image.load("rsc/ball/Health.png")
        
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.value = 50
        self.damage = 50
        #arm.gun = self.kind
        
    def shiftX(self, amount):
        self.rect.x += amount 
        



