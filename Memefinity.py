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
from BetterBossMeme import *
from EndFlag import *

pygame.init()

clock = pygame.time.Clock()

width = 1280 
height = 720
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0


all = pygame.sprite.Group()
players = pygame.sprite.Group()
memes = pygame.sprite.Group()
bosses = pygame.sprite.Group()
walls = pygame.sprite.Group()
backgrounds = pygame.sprite.Group() 
bigwalls = pygame.sprite.Group()
movingObjects = pygame.sprite.Group()
bullets = pygame.sprite.Group()
pickups = pygame.sprite.Group()
goals = pygame.sprite.Group()
EndFlags = pygame.sprite.Group()
boss = pygame.sprite.Group()
bossbullets = pygame.sprite.Group()

PlayerMeme.containers = players, all
Arm.containers = players, all
Bullet.containers = bullets, movingObjects, all
BossBullet.containers = bossbullets, movingObjects, all
Background.containers = backgrounds, movingObjects, all
Meme.containers = memes, movingObjects, all
BossMeme.containers = bosses, movingObjects, all
Wall.containers = walls,movingObjects, all
Wall_5x5.containers = bigwalls, movingObjects, all
Ground.containers = walls, movingObjects, all
GunPickup.containers = pickups, movingObjects, all
Goal.containers = goals, movingObjects, all
EndFlag.containers = EndFlags, movingObjects, all

#video transcode command:
"""
ffmpeg -i memefinityloading.mp4 -vcodec mpeg1video -b:v 2048k -acodec libmp3lame -s 1280x720 -intra memefinityloading.mpg
"""

#pygame.mixer.quit()

movie = pygame.movie.Movie('rsc/memefinityloading.mpg')
movie_screen = pygame.Surface(size)
movie_rect = movie_screen.get_rect()
movie.set_display(movie_screen)
movie.play()
pygame.mixer.music.load("rsc/audio/Intro Music.ogg")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            pygame.mixer.music.stop()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                movie.stop()
                pygame.mixer.music.stop()
                playing = False
    
    if not movie.get_busy() and playing:
        movie.stop()
        playing = False
    screen.blit(movie_screen, movie_rect)
    pygame.display.update()
    clock.tick(60)

while True:
    menu = True
    bg = Background("playbutton.png", size)
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu = False
        screen.blit(bg.image, bg.rect)
        pygame.display.update()
        clock.tick(60)
        
    levelNumber = 1 #REMOVE THIS IT WILL CAUSE PROBLEMS IN THE LATER

    bg = Background("BgLevel1.png")
    level = Level(levelNumber, size)
    
        
    if levelNumber == 2:
        level = Level(levelNumber, size)
        bg = Background("BgLevel1.png")
        
    if levelNumber == 3:
        level = Level(levelNumber, size)
        bg = Background("BgLevel1.png")


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
    
    pygame.mixer.music.load("rsc/audio/Level "+ str(levelNumber) + " Audio.ogg")
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    print "Volume:", pygame.mixer.music.get_volume()
    print "Is playing:", pygame.mixer.music.get_busy()
    
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
                    if event.key == pygame.K_m:
                        print "music pos: ", pygame.mixer.music.get_pos()
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
                        shooting = "alt"
                    if event.button == 2:
                        shooting = "beam"
                    if event.button == 3:
                        shooting = "alt"
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        shooting = None
                    if event.button == 2:
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
            #elif shooting == "beam":
                #if fireTimer < fireRate:
                    #fireTimer += 1
                #else:
                    #fire = 0
                    #Bullet(player.rect.center, arm.angle)

        if debug: print "after input handled: ", time.time() - startTime

        player.update(walls)
        arm.update()
        for bullet in bullets:
            bullet.update()
        for bossbullet in bossbullets:
            bossbullet.update()
        for meme in memes:
            meme.update(walls)
            meme.bounceScreen(size)
        for boss in bosses:
            boss.update(walls, player)
            boss.bounceScreen(size)

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
        memesHit = pygame.sprite.spritecollide(player, memes, True)
        bulletsHitMemes = pygame.sprite.groupcollide(bullets, memes, True, True)
        bulletsHitWalls = pygame.sprite.groupcollide(bullets, walls, True, False)
        playerHitspickups = pygame.sprite.spritecollide(player, pickups, True) 
        playerHitgoals = pygame.sprite.spritecollide(player, goals, False) 
        playerHitsbosses = pygame.sprite.spritecollide(player, bosses, False)
        bulletsHitbosses = pygame.sprite.groupcollide(bullets, bosses, True, False)
        playerHitbossbullets = pygame.sprite.spritecollide(player, bossbullets, True)
        bossbulletsHitWalls = pygame.sprite.groupcollide(bossbullets, walls, True, False)
        PlayerHitsEndFlag = pygame.sprite.spritecollide(player, EndFlags, False)

        
        if debug: print "after collision groups created: ", time.time() - startTime
        
        for meme in memesHit:
            meme.bounceMeme(PlayerMeme)
            player.hitMeme(meme)
            meme.speedx = -meme.speedx
            
        for boss in playerHitsbosses:
            player.hitMeme(boss)
            
        for EndFlag in PlayerHitsEndFlag:
            player.hitMeme(boss)
        
        for bullet in bulletsHitbosses:
            for boss in bulletsHitbosses[bullet]:
                boss.hitBullet(bullet)
                
        for bossbullet in playerHitbossbullets:   
            player.hitBossbullet(bossbullet)
        
        for pickup in playerHitspickups: 
            player.heal(pickup.value)
            
        
        for goal in playerHitgoals:
            level.unloadLevel(all)
            levelNumber += 1
            level = Level(levelNumber, size)
            bg = Background("BgLevel1.png")
            for p in players.sprites():
                if p.kind == "arm":
                    arm = p
                else:
                    player = p
            pygame.mixer.music.load("rsc/audio/Level "+ str(levelNumber) + " Audio.ogg")
            pygame.mixer.music.play(-1)
            print pygame.mixer.music.get_volume()
            print pygame.mixer.music.get_busy()
            
        #https://github.com/KRHS-GameProgramming-2016/Spikes-Evil-Maze-Game/blob/master/Game.py#L65
        
        
        if debug: print "after meme/player collision group: ", time.time() - startTime
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bg.image, bg.rect)
        if debug: print "after bg render: ", time.time() - startTime
        for meme in memes:
            screen.blit(meme.image, meme.rect)
        for meme in bosses:
            screen.blit(meme.image, meme.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for bossbullet in bossbullets:
            screen.blit(bossbullet.image, bossbullet.rect)
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
    
    level.unloadLevel(all) 
    
while BetterBossMeme.living :
    shooting ="alt" 


    
    
    
    
