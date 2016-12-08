import pygame, sys, math 

class Bullet():
    def __init__(self, pos, angle):
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()
        self.living = True
        self.angle = angle
        self.speedx = math.cos(math.radians(self.angle))*10
        self.speedy = -math.sin(math.radians(self.angle))*10
        self.rot_angle = self.angle - 90
        rot_image = pygame.transform.rotate(self.image, self.rot_angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        self.place(pos)
        self.radius = self.rect.height/2 
        
    def update(self):
        self.move() 
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed) 
        
    def collideMonster(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    other.living = False
                    self.living = False 
                    
    def collideWall(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.living = False
        if self.rect.top < 0 or self.rect.bottom > height:
            self.living = False 
            
    def place(self, pos):
        self.rect.center = pos 
        
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2)) #https://github.com/scscorley/jellitubby-attack/blob/master/Bullet.py 
        

