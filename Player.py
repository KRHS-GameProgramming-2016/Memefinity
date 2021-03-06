import pygame, sys, math
from Meme import *

class PlayerMeme(pygame.sprite.Sprite):
    def __init__(self, screensize, maxSpeed = 2, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.kind = "body"
        self.maxSpeed = maxSpeed     
        self.restRight = [pygame.transform.scale(pygame.image.load("rsc/ball/restright.png"), [100,100])]
        self.restLeft = [pygame.transform.scale(pygame.image.load("rsc/ball/restleft.png"), [100,100])]
        self.runRight = [pygame.transform.scale(pygame.image.load("rsc/ball/runright1.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright2.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright3.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright4.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright5.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright6.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright7.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright8.png"), [100, 100])
                        ]
        self.runLeft = [pygame.transform.scale(pygame.image.load("rsc/ball/runleft1.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft2.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft3.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft4.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft5.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft6.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft7.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft8.png"), [100, 100])
                        ]
        self.runBackLeft = [pygame.transform.scale(pygame.image.load("rsc/ball/runright8.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright7.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright6.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright5.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright4.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright3.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright2.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runright1.png"), [100, 100])
                        ]
        self.runBackRight = [pygame.transform.scale(pygame.image.load("rsc/ball/runleft8.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft7.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft6.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft5.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft4.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft3.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft2.png"), [100, 100]),
                        pygame.transform.scale(pygame.image.load("rsc/ball/runleft1.png"), [100, 100])
                        ]
        self.state = "rest right"
        self.prevState = "rest right"
        self.images = self.restRight
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.speedx = 0
        self.speedy = 0
        self.face = "right"
        self.side = "right"
        self.angle = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/3 -1
        self.didBounceX = False
        self.didBounceY = False
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .05 * 60 #seconds * 60 fps
        self.screenHeight = screensize[1]
        self.hp = 100
        self.living = True
        
    
    def heal(self, amount):
        self.hp += amount
    
    def playerSpeedx(self):
            return self.speedx

    def hitMeme(self, meme):
        self.hp -= meme.damage
        print self.hp

    def hitBossbullet(self, bossbullets):
        self.hp -= bossbullets.damage
        print self.hp
        
    def update(self, walls):
        # Gravity
        if self.hp <= 0:
            self.living = False
        self.animate()
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.speedx
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.speedx > 0:
                self.rect.right = block.rect.left
            elif self.speedx < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.speedy
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.speedy > 0:
                self.rect.bottom = block.rect.top
            elif self.speedy < 0:
                self.rect.top = block.rect.bottom
            # Stop our vertical movement
            self.speedy = 0
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.speedy == 0:
            self.speedy = 1
        else:
            self.speedy += .35
        # See if we are on the ground.
        if self.rect.bottom >= self.screenHeight and self.speedy >= 0:
            self.speedy = 0
            self.rect.bottom = self.screenHeight
            self.hp = 0
    
    def getPos(self, key="center"):
        if key == "center":
            return self.rect.center
        
            
    def animate(self):
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "run right":
                self.images = self.runRight
            if self.state == "run left":
                self.images = self.runLeft
            if self.state == "run back right":
                self.images = self.runBackRight
            if self.state == "run back left":
                self.images = self.runBackLeft
            if self.state == "rest right":
                self.images = self.restRight
            if self.state == "rest left":
                self.images = self.restLeft
                
            self.frame = 0
            self.maxFrame = len(self.images) - 1
            self.image = self.images[self.frame]
        
        if self.animationTimer < self.animationTimerMax:
            self.animationTimer += 1
        else:
            self.animationTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
  
    def aim(self, mousePos):
        #finds which way a player is facing
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        if self.angle <= 180 and self.angle >= 90 or self.angle >= -180 and self.angle <= -90:
            self.side = "left"
            if self.state == "rest right":
                self.state = "rest left"
                self.prevState = "rest right"
            elif self.state == "run right":
                self.state = "run back left"
            elif self.state == "run back right":
                self.state = "run left"
        if self.angle > 0 and self.angle < 90 or self.angle < 0 and self.angle > -90:
            self.side = "right"
            if self.state == "rest left":
                self.state = "rest right"
                self.prevState = "rest left"
            elif self.state == "run left":
                self.state = "run back right"
            elif self.state == "run back left":
                self.state = "run right"
        
            

        
        
    
    def go(self, direction, walls = None):
        if direction == "up":
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, walls, False)
            self.rect.y -= 2
            #print len(platform_hit_list)
            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= self.screenHeight:
                self.speedy = -10
        if direction == "left" and self.side == "left":
            self.speedx = -self.maxSpeed
            self.state = "run left"
            print "running left"
        if direction == "right" and self.side == "right":
            self.speedx = self.maxSpeed 
            self.state = "run right"
            print "running right"
        if direction == "left" and self.side == "right":
            self.speedx = -self.maxSpeed
            self.state = "run back left"
            print "running left backwards"
        if direction == "right" and self.side == "left":
            self.speedx = self.maxSpeed
            self.state = "run back right"
            print "running right backwards"

            
        if direction == "stop left":
            self.speedx = 0
            self.state = "rest left"
        if direction == "stop right":
            self.speedx = 0
            self.state = "rest right"
    
    def goMouse(self, pos):
        self.rect.center = pos
        
    
