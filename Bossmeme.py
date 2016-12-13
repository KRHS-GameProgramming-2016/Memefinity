import pygame, sys, math


class BossMeme(pygame.sprite.Sprite):
    def __init__(self, screensize, levelNumber, speed=[0,0], pos=[0,0], size=None):
        #print screensize, levelNumber
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("rsc/levelmat" + str(levelNumber) + "/meme/bossmeme.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2 -1
        self.didBounceX = False
        self.didBounceY = False
        self.screenHeight = screensize[1]

    def shiftX(self, amount):
        self.rect.x += amount
    
    def getPos(self, key="center"):
        if key == "center":
            return self.rect.center
        
    def update(self, walls):
       
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
            
    def jump(self, walls):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, walls, False)
        self.rect.y -= 2
        #print len(platform_hit_list)
        if len(platform_hit_list) > 0 or self.rect.bottom >= self.screenHeight:
            self.speedy = -10    
            
    def calc_grav(self):
        if self.speedy == 0:
            self.speedy = 1
        else:
            self.speedy += .35
        if (self.rect.y >= (self.screenHeight - self.rect.height)) and (self.speedy >= 0):
            self.speedy = 0
            self.rect.y = self.screenHeight - self.rect.height  
    
        
    def animate(self):
        if self.animationTimer < self.animationTimerMax:
            self.animationTimer += 1
        else:
            self.animationTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.didBounceY = True
            
    def bounceBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.dist(other.rect.center) < self.radius + other.radius:
                    if not self.didBounceX:
                        self.speedx = -self.speedx
                    if not self.didBounceY:
                        self.speedy = -self.speedy
        
    def dist(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        xDiff = x1 - x2
        yDiff = y1 - y2
        return math.sqrt(xDiff**2 + yDiff**2)  

#
