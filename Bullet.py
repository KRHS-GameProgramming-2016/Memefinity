#https://github.com/scscorley/jellitubby-attack/blob/master/Vacuum.py
import pygame, sys, math 


class Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.runRight = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArm" +self.gun+".png"), [100,100])
        self.runLeft = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArmLeft.png"), [100,100])
        self.restRight = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArm.png"), [100,100])
        self.restLeft = pygame.transform.scale(pygame.image.load("rsc/ball/PlayerArmLeft.png"), [100,100])
        self.gun = "M4A1"
        self.baseImage = self.restRight
        self.image = self.baseImage
        self.state = "rest right"
        self.prevState = "rest right"
        self.offset = [43,36]
        self.rect = self.image.get_rect()
        self.angle =0


        
    def aim(self, mousePos):
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
    
    def addOffsets(self):
        #print self.rect.center,
        self.rect.center = [self.player.rect.x+self.offset[0], 
                            self.player.rect.y+self.offset[1]]
        #print self.offset,  self.rect.center
    
    def update(self):
        self.state = self.player.state
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "run right":
                self.baseImage = self.runRight
                self.offset = [36,36]
            if self.state == "run left":
                self.baseImage = self.runLeft
                self.offset = [53,36]
            if self.state == "rest right":
                self.baseImage = self.restRight
                self.offset = [43,36]
            if self.state == "rest left":
                self.baseImage = self.restLeft
                self.offset = [58,36]
            self.image = self.baseImage
        self.addOffsets()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load("rsc/ball/bullet.png"), [10, 10])
        self.rect = self.image.get_rect()
        self.living = True
        self.angle = angle
        self.bulletSpeed = 40
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
        self.timerMax = 2*60
        
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
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2)) #https://github.com/scscorley/jellitubby-attack/blob/master/Bullet.py  

        

