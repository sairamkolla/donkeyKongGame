import pygame
from pygame.locals import *
running_img=pygame.image.load('mario_running.png')
running_img=pygame.transform.scale(running_img,(25,39))
standing_img=pygame.image.load('mario.png')
standing_img=pygame.transform.scale(standing_img,(25,39))
border_width=30
class player:
    def __init__(self,score,lives):
        self.startx=30
        self.starty=955
        self.x=30
        self.y=955
        self.rect=pygame.Rect(30,900,25,39)
        self.width=25
        self.height=39
        self.speedx=5
        self.speedy=5
        self.ladder=0
        self.ladderup=0
        self.ladderup=0
        self.jumpcount=0
        self.running=0
        self.on_the_floor=1
        self.floor_to_hit=0
        self.in_the_air=0
        self.score=score
        self.lives=10
        self.dy=0
        self.success=0
        return
    def update(self,screen,border_array,floor_mainarray,ladder_array,screen_width):
        #print '%d %d' %(self.x,self.y)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.ladder_set(ladder_array)
        #print self.jumpcount
        #print 'jumpcount is %d and dy is %d and on_the_floor is %d ' %(self.jumpcount,self.dy,self.on_the_floor)
        if not self.dy==0:
            #print self.dy
            #print 'hola'
            #print 'mario not inside ladder'
            if self.dy > 0:
                #print 'mario going down'
                if self.jumpcount==10:
                    self.dy=0
                    self.check_on_the_floor(floor_mainarray)
                    self.jumpcount=0
                else:
                    self.y+=5
                    self.jumpcount+=1
            elif self.dy <0:
                if self.jumpcount==10:
                    #print 'reached maximum height'
                    self.jumpcount=0
                    self.dy = -self.dy
                else:
                    #print 'going down'
                    self.y-=5
                    self.jumpcount+=1
            self.adjust_irregularities(floor_mainarray)
        if self.on_the_floor==0 and self.ladder==0 and self.dy==0:
            #print 'we are doing the shit floor=%d dy=%d' %(self.on_the_floor,self.dy)
            self.y+=5
            self.check_on_the_floor(floor_mainarray)
        for wall in border_array:
            if self.rect.colliderect(wall) and (wall[0]==0 or wall[0] >= screen_width-border_width):
                #print wall
                self.x=wall[0]-self.width if not wall[0]==0 else wall[0]+border_width
                #print 'collision happening'
                break
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if self.running:
            mario_img=running_img
        else:
            mario_img=standing_img
        screen.blit(mario_img,(self.x,self.y))
        return
    def adjust_irregularities(self,floor_mainarray):
        if 1:
            for floor in floor_mainarray:
                if abs(floor[1]-self.y-self.height) < 5 and not floor[1]-self.y-self.height==0 and self.x > floor[0] and self.x < floor[0]+floor[2]: #and floor[1]-self.y-self.height >=0:
                    #print 'done'
                    #print 'something adjusted'
                    self.y=floor[1]-self.height
                    self.on_the_floor=1
                    self.dy=0
                    break
        return
    def check_on_the_floor(self,floor_mainarray):
        for floor in floor_mainarray:
            if floor[1]==self.y+self.height and ((self.x >=floor[0] and self.x < floor[0]+floor[2]) or (self.x <=floor[0]+floor[2] and self.x+self.width > floor[0])):
                self.on_the_floor=1
                self.dy=0
                break
            else:
                self.on_the_floor=0
        return
    def ladder_set(self,ladder_array):
        for ladder in ladder_array:
            if self.x >= ladder[0] and self.x+self.width <= ladder[0] + ladder[2] and self.y+self.height <= ladder[1]+ladder[3] and not ladder[1] >= self.y+self.height:
                self.ladder=1
                self.ladderup=1
                #print 'ladder is 1 and up'
                break
            elif self.x >=ladder[0] and self.x + self.width <=ladder[0] +ladder[2] and self.y+self.height < ladder[1]+ladder[3] and  self.y+self.height >= ladder[1]:
                self.ladder=1
                self.ladderdown=1
                #print 'ladder is 1 and down'
                break
            else:
                self.ladder=0
                self.ladderup=0
                self.ladderdown=0
        return
