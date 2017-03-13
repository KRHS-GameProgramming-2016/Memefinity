import pygame, sys, math 

class BossMeme(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/ball/ball.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size*10,size*10])
        self.rect = self.image.get_rect(center = pos)
        self.damage = 10000
        self.hp = 500
    
    def shiftX(self, amount):
        self.rect.x += amount
        
    def hitBullet(self, bullet):
        self.hp -= bullet.damage
        if self.hp <= 0:
            self.kill()
