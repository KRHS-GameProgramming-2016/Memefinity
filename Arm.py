import pygame, sys, math

class Arm():
    def _init_(self, screensize, player):
        self.player = player
        self.baseImage = pygame.image.load("rsc/ball/PlayerArm.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect()
    
    def aim(self, mousePos):           #http://pygame.org/wiki/RotateCenter?parent=
        """rotate an image while keeping its center and size"""
        self.angle = 0 #trig from mousePos
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image
