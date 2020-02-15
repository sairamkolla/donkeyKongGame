import pygame
from pygame import *
from random import randint
from villians import *
RIGHT=1
LEFT=-1
coin_img=pygame.image.load('bcoin.png')
coin_img=pygame.transform.scale(coin_img,(30,30))
life_img=pygame.image.load('heart.png')
life_img=pygame.transform.scale(life_img,(25,25))
donkey_img=pygame.image.load('donkey.png')
donkey_img=pygame.transform.scale(donkey_img,(30,30))

class gold:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.done=0
        self.rect=pygame.Rect(x,y,30,30)
    def update(self,screen):
        if not self.done:
            screen.blit(coin_img,(self.x,self.y))
        return
class control:
    def __init__(self):
        return
    def coins(self,floor_mainarray,screen_width):
        coin_array=[]
        count=0
        for floor in floor_mainarray:
            coincount=randint(1,5)
            for i in range(coincount):
                x=randint(floor[0],floor[0]+floor[2]-30)
                if x < border_width:
                    x=border_width+30
                if x > screen_width-border_width-coin_img.get_width():
                    x =screen_width-border_width-coin_img.get_width()

                coin_array.insert(count,gold(x,floor[1]-30))
                count+=1
        return coin_array
    def coin_refresh(self,screen,coin_array,mario):
        for coin in coin_array:
            if coin.rect.colliderect(mario.rect) and not coin.done:
                coin.done=1
                mario.score+=1
            coin.update(screen)
        return
    def hearts(self,floor_mainarray,screen_width):
        __no_of_lives=10
        heart_array=[]
        count=0
        for __i in range(__no_of_lives):
            rand1=randint(0,len(floor_mainarray)-1)
            x=randint(floor_mainarray[rand1][0],floor_mainarray[rand1][0]+floor_mainarray[rand1][2]-life_img.get_width())
            if x < border_width:
                x=border_width+30
            if x > screen_width-border_width-life_img.get_width():
                x =screen_width-border_width-life_img.get_width()
            heart_array.insert(count,lives(x,floor_mainarray[rand1][1]-life_img.get_height()))
            count+=1
        return heart_array
    def heart_refresh(self,screen,heart_array,mario):
        for heart in heart_array:
            if heart.rect.colliderect(mario.rect) and not heart.taken:
                heart.taken=1
                mario.lives+=1
            heart.update(screen)
        return
    def create_donkey(self,count):
        donkey_array=[]
        for i in range(count):
            donkey_array.append(donkey_kong(30,200-donkey_img.get_height(),donkey_img.get_width(),donkey_img.get_height()))
        return donkey_array
    def donkey_refresh(self,screen,donkey_array,mario,ladder_array,floor_mainarray):
        for donkey in donkey_array:
            if donkey.rect.colliderect(mario.rect):
                mario.x=mario.startx
                mario.y=mario.starty
                mario.lives-=1
                mario.jumpcount=0
                mario.running=0
                mario.on_the_floor=1
                mario.dy=0
                mario.sucess=0
                mario.rect=pygame.Rect(30,900,25,39)
                print 'barre champindhi'

            donkey.update()
            screen.blit(donkey_img,(donkey.x,donkey.y))
            donkey.fireballs(screen,mario,ladder_array,floor_mainarray)
        return
    def information(self,screen,screen_width,border_width,border_height,mario):
        screen.blit(life_img,(screen_width-border_width-70,border_height))
        screen.blit(coin_img,(screen_width-border_width-140,border_height))
        screen.blit(pygame.font.SysFont('Arial', 25).render(str(mario.lives), True, (255,0,0)), (screen_width-border_width-70+30 , border_height+5))
        screen.blit(pygame.font.SysFont('Arial', 25).render(str(mario.score), True, (255,215,0)), (screen_width-border_width-140+35 , border_height+5))
        return
    def princess(self,screen,mario):
        princess_img=pygame.image.load('princess.png')
        princess_img=pygame.transform.scale(princess_img,(25,39))
        self.rect=pygame.Rect(30,161,25,39)
        screen.blit(princess_img,(30,161))
        if self.rect.colliderect(mario.rect):
            print 'devuda please.......'
            mario.success=1
class lives:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.taken=0
        self.rect=pygame.Rect(x,y,life_img.get_width(),life_img.get_height())
    def update(self,screen):
        if not self.taken:
            screen.blit(life_img,(self.x,self.y))
        return


        
