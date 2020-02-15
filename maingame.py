import pygame
from pygame import *
class board:
    def __init__(self):
        self.level=1
        return
    def construct(self,screen,screen_width,screen_height):
        #####--------------Making Border Array-----------#####
        x=0
        y=0
        border_array=[]
        borderimg_size=30
        while y < screen_height :
            border_array.append(pygame.Rect(0,y,borderimg_size,borderimg_size))
            border_array.append(pygame.Rect(screen_width-borderimg_size,y,borderimg_size,borderimg_size))
            y+=borderimg_size
        while x < screen_width :
            border_array.append(pygame.Rect(x,0,borderimg_size,borderimg_size))
            border_array.append(pygame.Rect(x,screen_height-borderimg_size,borderimg_size,borderimg_size))
            x+=borderimg_size
            ###------------Making Floor Array-----------###
        #a=[(30,850,900),(30,730,810),(200,570,500),(30,450,300),(525,450,400),(30,300,964)]
        a=[(10,850,964),(10,710,300),(600,710,400),(200,540,550),(10,350,250),(370,350,300),(750,350,300),(10,200,964)]
        floor_array=[]
        brickimg_length=65
        brickimg_height=25
        for x in a:
            start=x[0]
            m=0
            while m < x[2]:
                floor_array.append(pygame.Rect(start+m,x[1],brickimg_length,brickimg_height))
                m+=brickimg_length
        ###--------Making Ladder Array-------###
        ladder_array=[]
        a.insert(0,(30,994,994))
        floor_array.insert(0,(30,994,994))
        #print llm
        b=[(690,850,35,144),(900,710,35,140),(700,540,35,170),(240,540,35,170),(340,450,35,90),(625,350,35,190),(500,200,35,150),(900,200,35,150)]
        for ladder in b:
            ladder_array.append(pygame.Rect(ladder[0],ladder[1],ladder[2],ladder[3]))
            #pygame.draw.rect(screen,WHITE,(ladder[0],ladder[1],ladder[2],ladder[3]))
        return border_array,floor_array,ladder_array,a
    def background(self,screen,color):
        screen.fill(color)
        return
    def border(self,screen,border_array):
        borderimg=pygame.image.load('border.png')
        for x in border_array:
            screen.blit(borderimg,(x[0],x[1]))
        return border_array
    def platform(self,screen,floor_array):#floor format --> (x-corordinate,y-corordinate,length of floor)
        brickimg=pygame.image.load('brick.gif')
        for x in floor_array:
            screen.blit(brickimg,(x[0],x[1]))
        return
    def divider(self,screen,color):
        pygame.draw.rect(screen,color,[30,150,964,5])
        return
    def ladder(self,screen,ladder_array):
        WHITE=(255,255,255)
        for __ladder in ladder_array:
            pygame.draw.rect(screen,WHITE,(__ladder[0],__ladder[1],__ladder[2],__ladder[3]))
        return
    def refresh(self,screen,border_array,floor_array,ladder_array):
        BLACK=(0,0,0)
        self.background(screen,BLACK)
        self.platform(screen,floor_array)
        self.border(screen,border_array)
        self.ladder(screen,ladder_array)
        return
