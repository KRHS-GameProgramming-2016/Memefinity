debug = False 

import pygame, sys, math, random, time
from Meme import *
from Bossmeme import *
from Wall import *
from Level import *
from Player import *
from Arm import * 
from Bullet import *
from GunPickup import *
from Goal import *
pygame.init()

clock = pygame.time.Clock()

width = 1280 
height = 720
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0


all = pygame.sprite.Group()
players = pygame.sprite.Group()
balls = pygame.sprite.Group()
walls = pygame.sprite.Group()
backgrounds = pygame.sprite.Group() 
bigwalls = pygame.sprite.Group()
movingObjects = pygame.sprite.Group()
bullets = pygame.sprite.Group()
pickups = pygame.sprite.Group()
goals = pygame.sprite.Group()

PlayerMeme.containers = players, all
Arm.containers = players, all
Bullet.containers = bullets, movingObjects, all
Background.containers = backgrounds, movingObjects, all
Meme.containers = balls, movingObjects, all
Wall.containers = walls,movingObjects, all
Wall_5x5.containers = bigwalls, movingObjects, all
Ground.containers = walls, movingObjects, all
GunPickup.containers = pickups, movingObjects, all
Goal.containers = goals, movingObjects, all

levelNumber = 1 #REMOVE THIS IT WILL CAUSE PROBLEMS IN THE LATER


bg = Background("BgLevel1.png")
level = Level(levelNumber, size)
    
if levelNumber == 2:
    level = Level(levelNumber, size)
    
if levelNumber == 3:
    level = Level(levelNumber, size)


print len(walls.sprites())

#Meme(size, 1, 
              #[random.randint(1, 10), random.randint(1, 10)],
              #[random.randint(0, width-100), random.randint(0, height-100)],
              #random.randint(20, 100))
              
#player = PlayerMeme(size, 5, [width/2+50,height/2])
#arm = Arm(size, player)
using = "keyboard"

for p in players.sprites():
    if p.kind == "arm":
        arm = p
    else:
        player = p
glev = 0

print player, arm

shooting = None
rightIsDown = False
leftIsDown = False
downLast = "right"

if debug: startTime = time.time()

fireRate = arm.gun.fireRate
fireTimer = 0

print "Pickups: ", pickups.sprites()[0].rect.center
print "player: ", players.sprites()[0].rect.center

while player.living :
    if debug: print "last loop total: ", time.time() - startTime
    if debug: print "--------------------------------------------------------------------------------"
    if debug: startTime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.go("up", walls)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    rightIsDown = True
                    downLast = "right"
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    leftIsDown = True
                    downLast = "left"
                if event.key == pygame.K_u:
                    print player.playerSpeedx()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    rightIsDown = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    leftIsDown = False
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(True)
                arm.aim(event.pos)
                player.aim(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shooting = "normal"
                if event.button == 3:
                    shooting = "alt"
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    shooting = None
                if event.button == 3:
                    shooting = None
    
    if debug: print "after events: ", time.time() - startTime
    if rightIsDown and not leftIsDown:
        player.go("right")
    elif leftIsDown and not rightIsDown:
        player.go("left")
    elif rightIsDown and leftIsDown:
        player.go(downLast)
    else:
        player.go("stop "+downLast)
        
    if shooting:
        if shooting == "normal":
            Bullet(player.rect.center, arm.angle)
            shooting = None
        elif shooting == "alt":
            if fireTimer < fireRate:
                fireTimer += 1
            else:
                fireTimer = 0
                Bullet(player.rect.center, arm.angle)

    if debug: print "after input handled: ", time.time() - startTime

    player.update(walls)
    arm.update()
    for bullet in bullets:
        bullet.update()
    for ball in balls:
        ball.update(walls)
        ball.bounceScreen(size)

    if debug: print "after updates done: ", time.time() - startTime
    
    if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            level.shiftWorld([movingObjects], -diff)
    if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            level.shiftWorld([movingObjects], diff)


    if debug: print "after scrolling done: ", time.time() - startTime
    ballsHit = pygame.sprite.spritecollide(player, balls, True)
    bulletsHitBalls = pygame.sprite.groupcollide(bullets, balls, True, True)
    abulletsHitWalls = pygame.sprite.groupcollide(bullets, walls, True, False)
    playerHitspickups = pygame.sprite.spritecollide(player, pickups, True) 
    playerHitgoals = pygame.sprite.spritecollide(player, goals, False) 
    
    if debug: print "after collision groups created: ", time.time() - startTime
    
    for ball in ballsHit:
        ball.bounceBall(PlayerMeme)
        player.hitBall(ball)
        ball.speedx = -ball.speedx
        
    for pickup in playerHitspickups: 
        player.heal(pickup.value)
        
    
    for goal in playerHitgoals:
        level.unloadLevel(all)
        levelNumber += 1
        if levelNumber == 2:
            level = Level(levelNumber, size)
        if levelNumber == 3:
            level = Level(levelNumber, size)
        for p in players.sprites():
            if p.kind == "arm":
                arm = p
            else:
                player = p
        
    #https://github.com/KRHS-GameProgramming-2016/Spikes-Evil-Maze-Game/blob/master/Game.py#L65
    
    
    if debug: print "after ball/player collision group: ", time.time() - startTime
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bg.image, bg.rect)
    if debug: print "after bg render: ", time.time() - startTime
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    for pickup in pickups:
        screen.blit(pickup.image, pickup.rect)
    screen.blit(player.image, player.rect)
    screen.blit(arm.image, arm.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    for wall in bigwalls:
        screen.blit(wall.image, wall.rect)
    for goal in goals:
        screen.blit(goal.image, goal.rect)
    pygame.display.flip()
    clock.tick(60)
    
    if debug: print "after render: ", time.time() - startTime, ", fps:", clock.get_fps()



 

    
    
    
    
    
