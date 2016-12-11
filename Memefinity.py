import pygame, sys, math, random
from Meme import *
from Bossmeme import *
from Wall import *
from Level import *
from Player import *
#from Arm import *
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
bigwalls = pygame.sprite.Group()
movingObjects = pygame.sprite.Group()

PlayerMeme.containers = players
#Arm.containers = players
Meme.containers = balls, movingObjects
Wall.containers = walls,movingObjects
Wall_5x5.containers = bigwalls, movingObjects


levelNumber = 1 #REMOVE THIS IT WILL CAUSE PROBLEMS IN THE LATER!

if levelNumber == 1:
    level = Level(levelNumber, size)
    
if levelNumber == 2:
    level = Level(levelNumber, size)
    
if levelNumber == 3:
    level = Level(levelNumber, size)

if levelNumber == 4:
    level = Level(levelNumber, size)

if levelNumber == 5:
    level = Level(levelNumber, size)

if levelNumber == 6:
    level = Level(levelNumber, size)

if levelNumber == 7:
    level = Level(levelNumber, size)

if levelNumber == 8:
    level = Level(levelNumber, size)

if levelNumber == 9:
    level = Level(levelNumber, size)

if levelNumber == 10:
    level = Level(levelNumber, size)


print len(walls.sprites())

#Meme(size, 1, 
              #[random.randint(1, 10), random.randint(1, 10)],
              #[random.randint(0, width-100), random.randint(0, height-100)],
              #random.randint(20, 100))
              
#player = PlayerMeme(size, 5, [width/2+50,height/2])
#arm = Arm(size, player)
using = "keyboard"

player = players.sprites()[0]
#arm = players.sprites()[1]
glev = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up", walls)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
            #if event.type == pygame.MOUSEMOTION:
                #pygame.mouse.set_visible(False)
                #player.goMouse(event.pos)

    
    player.update(walls)
#    arm.update()
    for ball in balls:
        ball.update(walls)
        ball.bounceScreen(size)

    if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            level.shiftWorld([movingObjects], -diff)
    if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            level.shiftWorld([movingObjects], diff)
    
    ballsHit = pygame.sprite.spritecollide(player, balls, False)
    
    for ball in ballsHit:
        ball.bounceBall(PlayerMeme)
        print"hit!!"
    
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
#    screen.blit(arm.image, arm.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    for wall in bigwalls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)

    
    
    
    
    
