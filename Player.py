import pygame, sys, math
from Meme import *

class PlayerBall(Ball):
    def __init__(self, screensize, maxSpeed =5, pos=[0,0]):
        Ball.__init__(self, "playerball_up_1.png", [0,0], pos, None)
        self.maxSpeed = maxSpeed     
        self.images = [pygame.image.load("rsc/ball/playerball_up_1.png"),
                       pygame.image.load("rsc/ball/playerball_up_2.png")
                      ]
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .2 * 60 #seconds * 60 fps
        self.screenHeight = screensize[1]
        
    def update(self, walls):
        # Gravity
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
        if self.rect.y >= self.screenHeight - self.rect.height and self.speedy >= 0:
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
        
    def go(self, direction, walls = None):
        if direction == "up":
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, walls, False)
            self.rect.y -= 2
            print len(platform_hit_list)
            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= self.screenHeight:
                self.speedy = -20
        if direction == "left":
            self.speedx = -self.maxSpeed
        if direction == "right":
            self.speedx = self.maxSpeed 
            
        if direction == "stop left":
            self.speedx = 0
        if direction == "stop right":
            self.speedx = 0
    
    def goMouse(self, pos):
        self.rect.center = pos
               
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
            self.didBounceY = True
            
