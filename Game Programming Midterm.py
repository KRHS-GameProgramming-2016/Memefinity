import pygame, sys, math, random

class BasicBall():
    def __init__(self, speed, image, pos, screenSize):
        self.image = pygame.transform.scale(pygame.image.load("you-win.png"), [100,100])
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(pos)
        self.radius = self.rect.width/2 -1
        self.didBounceX = False
        self.didBounceY = False
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        print self.speed
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def screenEdgeCollide(self):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.didBounceY = True
        
        
pygame.init()

clock = pygame.time.Clock()
width = 800   
height = 600



size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
# Image from: http://www.arborcollective.com/wp-content/uploads/2011/01/you-win.jpg
ball = BasicBall([60,60], "you-win.png", [width/2, height/2], size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ball.move()
    ball.screenEdgeCollide()
    if ball.didBounceX or ball.didBounceY:
        bgColor = r,g,b = random.randint(30, 255), random.randint(30, 255), random.randint(30, 255)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(ball.image, ball.rect)        
    pygame.display.flip()
    clock.tick(60)
    
    
    
