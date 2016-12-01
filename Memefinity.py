import pygame, sys, math, random
from Meme import *
from Bossmeme import *
from Wall import *
from Level import *
from Player import *
pygame.init()

clock = pygame.time.Clock()

width = 1280 
height = 720
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0

players = pygame.sprite.Group()
balls = pygame.sprite.Group()
walls = pygame.sprite.Group()

PlayerBall.containers = players
Ball.containers = balls
Wall.containers = walls

level = Level("level1.lvl")

Ball("ball.png", size,
              [random.randint(1, 10), random.randint(1, 10)],
              [random.randint(0, width-100), random.randint(0, height-100)],
              random.randint(20, 100))
              
player = PlayerBall(size, 5, [width/2,height/2])

using = "keyboard"

glev = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up", walls)
                if event.key == pygame.K_s:
                    player.go("down")
                if event.key == pygame.K_d:
                    player.go("right")
                if event.key == pygame.K_a:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.go("stop up")
                if event.key == pygame.K_s:
                    player.go("stop down")
                if event.key == pygame.K_d:
                    player.go("stop right")
                if event.key == pygame.K_a:
                    player.go("stop left")
        else:
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                player.goMouse(event.pos)
    
    if len(balls) == 0:
        glev += 1
        for b in range(glev):
            Ball("ball.png", size, 
                  [random.randint(1, 10), random.randint(1, 10)],
                  [random.randint(0, width-100), random.randint(0, height-100)],
                  random.randint(20, 100))
            if pygame.sprite.spritecollide(balls.sprites()[-1], walls, False):
                balls.sprites()[-1].kill()
                print "OH NOESSS!!!"
    
    for ball in balls:
        ball.update(walls)
        ball.bounceScreen(size)
        
    player.update(walls)
    player.bounceScreen(size)
    
    if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            level.shiftWorld([walls, balls], -diff)
    if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            level.shiftWorld([walls, balls], diff)
    
    ballsHit = pygame.sprite.spritecollide(player, balls, False)
    
    for ball in ballsHit:
        ball.kill()
    
    
    
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    
