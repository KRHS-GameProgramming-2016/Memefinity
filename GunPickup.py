import pygame, sys, math





class GunPickup(pygame.sprite.Sprite):
    def __init__(self, screensize, levelNumber, speed=[0,0], pos=[0,0], size=None):
        #print screensize, levelNumber
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/PlayerArm.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[0]
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2 -1
        self.didBounceX = False
        self.didBounceY = False
        self.screenHeight = screensize[1]
        self.damage = 50
    
