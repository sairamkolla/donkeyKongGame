import pygame
from pygame import *
from basic1 import *
from random import randint
RIGHT=1
LEFT=-1
DOWN=3
horizontal=[1,-1]
fire_img=pygame.image.load('fireball.png')
fire_img=pygame.transform.scale(fire_img,(15,15))
screen_width=1024
screen_height=1024
border_width=30
class missiles(basic):
    def __init__(self,x,y,w,h):
        basic.__init__(self,x,y,w,h)
        self.speedx=3
        self.speedy=3
        self.direction=RIGHT
        self.ladderdown=0
        self.alive=1
        return
    def update(self,screen,mario,ladder_array,floor_mainarray):
        if self.alive==1:
        #print('entered %d %d ' %(self.x,self.y))
            #print('entered %d %d ' %(self.width,self.height))
        #if self.direction==RIGHT:
        #    print('RIGHT')
            if self.x <border_width:
                #print('collision in the left')
                self.x=border_width
                self.direction=RIGHT
            elif self.x > screen_width-border_width:
                #print('collision in the right')
                self.x=screen_width-border_width
                self.direction=LEFT
            if self.rect.colliderect(mario) and self.alive==1:
                self.alive=0
                mario.x=mario.startx
                mario.y=mario.starty
                mario.lives-=1
                mario.jumpcount=0
                mario.running=0
                mario.on_the_floor=1
                mario.dy=0
                mario.sucess=0
                mario.rect=pygame.Rect(30,900,25,39)
            elif (self.x ==30 and self.y > 930 ) or self.y > 930 :
                self.alive=0
            self.check_on_the_floor(floor_mainarray)
            self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
            screen.blit(fire_img,(self.x,self.y))
            #-------------collisions takencareof------------###
            #self.adjust_irregularities(floor_mainarray)
            if self.direction==LEFT or self.direction==RIGHT:
                #if self.direction==RIGHT:
                #    print('RIGHT')
                self.ladder_set(ladder_array)
                if self.ladderdown==1:
                    rand1=randint(0,923479)

                    #rand1=0
                    #print('have a ladder chance')

                    if rand1%2:
                        #print('will move down in next iteration')
                        self.direction=DOWN
                        #self.y+=self.speedy
                        self.adjust_irregularities(floor_mainarray)
                    else:
                        #print('moving right')
                        self.x+=(self.direction*self.speedx)
                else:
                    #print('moving right')
                    self.x+=(self.direction*self.speedx)
            elif self.direction==DOWN:
                #print('going down')
                self.y+=5
                #self.y+=self.speedy
                self.adjust_irregularities(floor_mainarray)
            #print('exited %d %d ' %(self.x,self.y))
        return
    def check_on_the_floor(self,floor_mainarray):
        flag=0
        for floor in floor_mainarray:
            if floor[1]==self.y+self.height-1 and ((self.x >=floor[0] and self.x < floor[0]+floor[2]) or (self.x <=floor[0]+floor[2] and self.x+self.width > floor[0])):
                #self.direction=horizontal[randint(0,1)]
                flag=1
        if not flag==1:
            self.direction=DOWN
        return
    def adjust_irregularities(self,floor_mainarray):
        for floor in floor_mainarray:
            #print(floor[1]-self.y-self.height)
            #if floor[1]-(self.y+self.height-1) <=self.speedy and floor[1]-self.y-self.height>1 :#and self.x > floor[0] and self.x < floor[0]+floor[2]: #and floor[1]-self.y-self.height >=0:
            if floor[1]-(self.y+self.height-1) <=5 and floor[1]-self.y-self.height>1 :#and self.x > floor[0] and self.x < floor[0]+floor[2]: #and floor[1]-self.y-self.height >=0:
                    #print('done')

                #print('something adjusted')
                self.y=floor[1]-self.height+1
                if self.direction==DOWN:
                    #self.direction=RIGHT
                    self.direction=horizontal[randint(0,1)]
                break
        return
    def ladder_set(self,ladder_array):
        #print('this function is called')
        for ladder in ladder_array:
            if self.x >=ladder[0] and self.x + self.width <=ladder[0] +ladder[2] and self.y+self.height -1 < ladder[1]+ladder[3]-1 and  self.y+self.height >= ladder[1]:
                #self.ladder=1
                self.ladderdown=1
                #print(self.direction)
                #print('yes!!')
                break
            else:
                #print('no')
                self.ladder=0
                self.ladderdown=0
        #print('bye bye')
        return
class donkey_kong(basic):
    def __init__(self,x,y,w,h):
        basic.__init__(self,x,y,w,h)
        self.count=0
        self.firearray=[]
        self.direction=horizontal[randint(0,876426)%2]
        self.speedx=randint(1,3)
        return
    def fireballs(self,screen,mario,ladder_array,floor_mainarray):
        #print(len(self.firearray))
        if self.count==100:
            self.count=0
            self.firearray.insert(0,missiles(self.x,self.y+100-14,15,15))
            #print('new ball created')
        self.count+=1
        for fireball in self.firearray:
            fireball.update(screen,mario,ladder_array,floor_mainarray)
            #print('done')
        return
    def update(self):
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if self.x <border_width:
            #print('collision in the left')
            self.x=border_width
            self.direction=RIGHT
        elif self.x > screen_width-self.width-border_width:
            #print('collision in the right')
            self.x=screen_width-self.width-border_width
            self.direction=LEFT
        self.x+=(self.direction*randint(0,10))#self.speedx)
        return
