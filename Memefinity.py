import pygame, sys, math, random
from Meme import *
from Bossmeme import *
from Wall import *
from Level import *
from Player import *
from Arm import * 
from Bullet import *
from GunPickup import *
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
backgrounds = pygame.sprite.Group() 
bigwalls = pygame.sprite.Group()
movingObjects = pygame.sprite.Group()
bullets = pygame.sprite.Group()
pickups = pygame.sprite.Group()

PlayerMeme.containers = players
Arm.containers = players
Bullet.containers = bullets, movingObjects
Background.containers = backgrounds, movingObjects
Meme.containers = balls, movingObjects
Wall.containers = walls,movingObjects
Wall_5x5.containers = bigwalls, movingObjects
Ground.containers = walls, movingObjects
GunPickup.containers = pickups, movingObjects

levelNumber = 1 #REMOVE THIS IT WILL CAUSE PROBLEMS IN THE LATER

if levelNumber == 1:
    bg = Background("bgtest.png")
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

for p in players.sprites():
    if p.kind == "arm":
        arm = p
    else:
        player = p
glev = 0

print player, arm

shooting = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.go("up", walls)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
                if event.key == pygame.K_u:
                    print player.playerSpeedx()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
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
        
    if shooting:
        if shooting == "normal":
            Bullet(player.rect.center, arm.angle)
            shooting = None
        elif shooting == "alt":
            Bullet(player.rect.center, arm.angle)

   
    player.update(walls)
    arm.update()
    for bullet in bullets:
        bullet.update()
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

    
    ballsHit = pygame.sprite.spritecollide(player, balls, True)
    bulletsHitBalls = pygame.sprite.groupcollide(bullets, balls, True, True)
    abulletsHitWalls = pygame.sprite.groupcollide(bullets, walls, True, False)
    playerHitspickups = pygame.sprite.spritecollide(player, pickups, True) 
    
    for ball in ballsHit:
        ball.bounceBall(PlayerMeme)
        player.hitBall(ball)
        ball.speedx = -ball.speedx
        
    for pickup in playerHitspickups: 
        if pickup.kind == "AK47": 
            arm.kind = "AK47"
        
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bg.image, bg.rect)
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
    pygame.display.flip()
    clock.tick(60)


 

    
    
    
    
    
