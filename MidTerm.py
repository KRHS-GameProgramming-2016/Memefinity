import sys, pygame
pygame.init() 

clock = pygame.time.Clock() 

width = 800 
height = 600 
size = width, height 
speedx = 5 
speedy = 10
speed = [speedx, speedy]
bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size) 

ball1 = pygame.image.load("rsc/ball/ball.png")
ball1rect = ball1.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ball1rect = ball1rect.move(speed)

    if ball1rect.left < 0 or ball1rect.right > width:
        speed[0] = -speed[0]

    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(ball1, ball1rect)
    pygame.display.flip()
    clock.tick(60) 
    
def bounceWall(self, size):
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
            
for ball in balls:
        ball.move()
        ball.bounceWall(size)
