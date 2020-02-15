import pygame
from pygame import *
class basic():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.rect=pygame.Rect(x,y,w,h)
        self.width=w
        self.height=h
        #return

