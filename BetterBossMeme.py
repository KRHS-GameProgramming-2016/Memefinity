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
        self.hp = 500
#        self.speedy = 0
#        self.screenHeight = screensize[1]
    
    def shiftX(self, amount):
        self.rect.x += amount
        
    def hitBullet(self, bullet):
        self.hp -= bullet.damage
        if self.hp <= 0:
            self.kill()

    def shiftX(self, amount):
        self.rect.x += amount
    
    #def getPos(self, key="center"):
        #if key == "center":
            #return self.rect.center
        
    #def update(self, walls):
       
        #self.calc_grav()
 
        #self.rect.x += self.speedx
 
        #block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        #for block in block_hit_list:
            #if self.speedx > 0:
                #self.rect.right = block.rect.left
                #self.jump(walls)
            #elif self.speedx < 0:
                #self.rect.left = block.rect.right
                #self.jump(walls)
 
        #self.rect.y += self.speedy
 
        #block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        #for block in block_hit_list:
            #if self.speedy > 0:
                #self.rect.bottom = block.rect.top
            #elif self.speedy < 0:
                #self.rect.top = block.rect.bottom
            #self.speedy = 0
            
    #def calc_grav(self):
        #if self.speedy == 0:
            #self.speedy = 1
        #else:
            #self.speedy += .35
        #if (self.rect.y >= (self.screenHeight - self.rect.height)) and (self.speedy >= 0):
            #self.speedy = 0
            #self.rect.y = self.screenHeight - self.rect.height 
