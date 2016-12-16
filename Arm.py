import pygame, sys, math

class Arm(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.baseImage = pygame.image.load("rsc/ball/PlayerArm.png")
        self.baseImage = pygame.transform.scale(self.baseImage, [100,100])
        self.image = self.baseImage
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
        self.rect.center = [self.player.rect.x+50, 
                            self.player.rect.y+38]

#
