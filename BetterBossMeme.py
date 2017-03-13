import pygame, sys, math
from Meme import *

class BossMeme(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/ball/ball.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size*10,size*10])
        self.rect = self.image.get_rect(center = pos)
        self.damage = 10000
        
    def shiftX(self, amount):
        self.rect.x += amount
