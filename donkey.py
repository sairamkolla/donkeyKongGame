import pygame
from pygame import *
from maingame import *
from mario import *
from properties import *
from villians import *
screen_width=1024
screen_height=1024
border_width=30
border_height=30
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.init()
FPS=30
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
clock=pygame.time.Clock()
x=board()
border_array,floor_array,ladder_array,floor_mainarray=x.construct(screen,screen_width,screen_height )
#print(border_array)
#print(floor_array)
mario=player(0,0)
operator=control()
coin_array=operator.coins(floor_mainarray,screen_width)
heart_array=operator.hearts(floor_mainarray,screen_width)
donkey_array=operator.create_donkey(x.level)
#mario_img=pygame.image.load('mario.png')
#mario_img=pygame.transform.scale(mario,(25,39))
def exit_screen():
    screen.fill(BLACK)
    screen.blit(pygame.font.SysFont('Arial', 25).render('you have failed your mission!!', True, (255,0,0)), (300,500))
    return
def success_screen():
    screen.fill(BLACK)
    screen.blit(pygame.font.SysFont('Arial', 25).render('Congrats mario!!,you have saved the princess and won  '+str(mario.score)+'  coins', True, (124,252,0)), (300,500))
    return
def refresh():
    if mario.success==1:
        #print('devudu karuninchadu')
        success_screen()
    elif mario.lives:
        x.refresh(screen,border_array,floor_array,ladder_array)
        mario.adjust_irregularities(floor_mainarray)
        mario.update(screen,border_array,floor_mainarray,ladder_array,screen_width)
    #mario.update(screen,border_array,floor_mainarray,ladder_array)
        operator.coin_refresh(screen,coin_array,mario)
        operator.heart_refresh(screen,heart_array,mario)
        operator.donkey_refresh(screen,donkey_array,mario,ladder_array,floor_mainarray)
        operator.information(screen,screen_width,border_width,border_height,mario)
        operator.princess(screen,mario)
    else:
        exit_screen()
        #screen.fill(BLACK)
    return
while 1: #the main loop
    refresh()
    mario.running=0
    changex=0
    changey=0
    for event in pygame.event.get():
        refresh()
        mario.running=0
        if event.type==QUIT:
            pygame.quit()
            sys.quit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                mario.ladder_set(ladder_array)
                if mario.dy==0:
                    mario.jumpcount=1
                    mario.y-=5
                    mario.dy=-1
            elif event.key==K_r:
                mario=player(0,0)
    key=pygame.key.get_pressed()
    ###----------for movement on ladder and floors-------------------------########
    if key[K_UP]:
        for ladder in ladder_array:
            if mario.x >= ladder[0] and mario.x+mario.width <= ladder[0] + ladder[2] and mario.y+mario.height <= ladder[1]+ladder[3] and not ladder[1] >= mario.y+mario.height:
                mario.ladder=1
                mario.y-=mario.speedy
                break
    elif key[K_DOWN]:
        #print('in down')
        for ladder in ladder_array:
            if mario.x >=ladder[0] and mario.x + mario.width <=ladder[0] +ladder[2] and mario.y+mario.height < ladder[1]+ladder[3] and  mario.y+mario.height >= ladder[1]:
                mario.ladder=1
                mario.y+=mario.speedy
                break
    elif key[K_LEFT]:
        mario.ladder_set(ladder_array)
        mario.check_on_the_floor(floor_mainarray)
        if mario.on_the_floor:
            mario.running=1
            mario.x-=mario.speedx
        elif not mario.ladder:
            mario.running=1
            mario.x-=mario.speedx
    elif key[K_RIGHT]:
        #print('in right')
        mario.ladder_set(ladder_array)
        mario.check_on_the_floor(floor_mainarray)
        if mario.on_the_floor:
            mario.running=1
            mario.x+=mario.speedx
        elif not mario.ladder:
            mario.running=1
            mario.x+=mario.speedx
    pygame.display.update()
    clock.tick(FPS)

