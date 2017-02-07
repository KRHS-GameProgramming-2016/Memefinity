
import pygame, sys, math, random

class Goal(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], tileSize = 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = pygame.image.load("rsc/ball/end_flag.png")
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos)
        
    def shiftX(self, amount):
        self.rect.x += amount 
