import pygame, sys, math

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/wall/wall.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        
    def shiftX(self, amount):
        self.rect.x += amount
    
class Wall_5x5(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/wall/wall.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size*5,size*5])
        self.rect = self.image.get_rect(center = pos)
        
    def shiftX(self, amount):
        self.rect.x += amount           

#
