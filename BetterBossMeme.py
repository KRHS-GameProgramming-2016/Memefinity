import pygame, sys, math
from Meme import *

class BossMeme(pygame.sprite.Sprite):
    def __init__(self, screensize, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/ball/trumpv1.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size*9,size*9])
        self.rect = self.image.get_rect(center = pos)
        self.damage = 10000
        self.hp = 500
        self.speedy = 0
        self.speedx = 5
        self.speed = [self.speedx, self.speedy]
        self.screenHeight = screensize[1]
    
    def shiftX(self, amount):
        self.rect.x += amount
        
    def hitBullet(self, bullet):
        self.hp -= bullet.damage
        if self.hp <= 0:
            self.kill()

    def shiftX(self, amount):
        self.rect.x += amount
    
    def getPos(self, key="center"):
        if key == "center":
            return self.rect.center
        
    def update(self, walls, player):
       
        self.calc_grav()
 
        self.rect.x += self.speedx
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.speedx > 0:
                self.rect.right = block.rect.left
                self.jump(walls)
            elif self.speedx < 0:
                self.rect.left = block.rect.right
                self.jump(walls)

        self.rect.y += self.speedy
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.speedy > 0:
                self.rect.bottom = block.rect.top
            elif self.speedy < 0:
                self.rect.top = block.rect.bottom
                self.speedy = 0
        
        posPlayer = player.getPos()        
        if self.dist(posPlayer) < 1000:
            posPlayerX = posPlayer[0]
            posPlayerY = posPlayer[1]
            self.angle = float(((math.atan2(posPlayerY, -posPlayerX))/math.pi)*240)
            self.angle = -self.angle
            print "shoot"
            BossBullet(self.rect.center, self.angle)
    
    def jump(self, walls):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, walls, False)
        self.rect.y -= 2
        #print len(platform_hit_list)
        if len(platform_hit_list) > 0 or self.rect.bottom >= self.screenHeight:
            self.speedy = -10  
    
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.didBounceY = True        
    
    def calc_grav(self):
        if self.speedy == 0:
            self.speedy = 1
        else:
            self.speedy += .35
        if (self.rect.y >= (self.screenHeight - self.rect.height)) and (self.speedy >= 0):
            self.speedy = 0
            self.rect.y = self.screenHeight - self.rect.height 
            
    def dist(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        xDiff = x1 - x2
        yDiff = y1 - y2
        return math.sqrt(xDiff**2 + yDiff**2)  
 
            
class BossBullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load("rsc/ball/bossbullet.png"), [50, 50])
        self.rect = self.image.get_rect()
        self.living = True
        self.angle = angle
        self.bulletSpeed = 20
        self.speedx = math.cos(math.radians(self.angle))* self.bulletSpeed
        self.speedy = -math.sin(math.radians(self.angle))* self.bulletSpeed
        self.rot_angle = self.angle - 90
        rot_image = pygame.transform.rotate(self.image, self.rot_angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        self.place(pos)
        self.radius = self.rect.height/2 
        self.timer = 0
        self.timerMax = 60
        self.damage = 50
        
    def update(self):
        self.move() 
        if self.timer < self.timerMax:
            self.timer += 1
        else:
            self.kill()
            
    def shiftX(self, amount):
        self.rect.x += amount 
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed) 
       
                    
    def collideWall(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.living = False
        if self.rect.top < 0 or self.rect.bottom > height:
            return True
        return False 
            
    
    def place(self, pos):
        self.rect.center = pos 
        
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
