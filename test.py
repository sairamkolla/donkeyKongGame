from maingame import *
from donkey import *
from villians import *
from basic1 import *
from mario import *
from properties import *
import pygame
ladder_array=[<rect(690, 850, 35, 144)>, <rect(900, 710, 35, 140)>, <rect(700, 540, 35, 170)>, <rect(240, 540, 35, 170)>, <rect(340, 450, 35, 90)>, <rect(625, 350, 35, 190)>, <rect(500, 200, 35, 150)>, <rect(900, 200, 35, 150)>]

floor_array=[(30, 994, 994), <rect(10, 850, 65, 25)>, <rect(75, 850, 65, 25)>, <rect(140, 850, 65, 25)>, <rect(205, 850, 65, 25)>, <rect(270, 850, 65, 25)>, <rect(335, 850, 65, 25)>, <rect(400, 850, 65, 25)>, <rect(465, 850, 65, 25)>, <rect(530, 850, 65, 25)>, <rect(595, 850, 65, 25)>, <rect(660, 850, 65, 25)>, <rect(725, 850, 65, 25)>, <rect(790, 850, 65, 25)>, <rect(855, 850, 65, 25)>, <rect(920, 850, 65, 25)>, <rect(10, 710, 65, 25)>, <rect(75, 710, 65, 25)>, <rect(140, 710, 65, 25)>, <rect(205, 710, 65, 25)>, <rect(270, 710, 65, 25)>, <rect(600, 710, 65, 25)>, <rect(665, 710, 65, 25)>, <rect(730, 710, 65, 25)>, <rect(795, 710, 65, 25)>, <rect(860, 710, 65, 25)>, <rect(925, 710, 65, 25)>, <rect(990, 710, 65, 25)>, <rect(200, 540, 65, 25)>, <rect(265, 540, 65, 25)>, <rect(330, 540, 65, 25)>, <rect(395, 540, 65, 25)>, <rect(460, 540, 65, 25)>, <rect(525, 540, 65, 25)>, <rect(590, 540, 65, 25)>, <rect(655, 540, 65, 25)>, <rect(720, 540, 65, 25)>, <rect(10, 350, 65, 25)>, <rect(75, 350, 65, 25)>, <rect(140, 350, 65, 25)>, <rect(205, 350, 65, 25)>, <rect(370, 350, 65, 25)>, <rect(435, 350, 65, 25)>, <rect(500, 350, 65, 25)>, <rect(565, 350, 65, 25)>, <rect(630, 350, 65, 25)>, <rect(750, 350, 65, 25)>, <rect(815, 350, 65, 25)>, <rect(880, 350, 65, 25)>, <rect(945, 350, 65, 25)>, <rect(1010, 350, 65, 25)>, <rect(10, 200, 65, 25)>, <rect(75, 200, 65, 25)>, <rect(140, 200, 65, 25)>, <rect(205, 200, 65, 25)>, <rect(270, 200, 65, 25)>, <rect(335, 200, 65, 25)>, <rect(400, 200, 65, 25)>, <rect(465, 200, 65, 25)>, <rect(530, 200, 65, 25)>, <rect(595, 200, 65, 25)>, <rect(660, 200, 65, 25)>, <rect(725, 200, 65, 25)>, <rect(790, 200, 65, 25)>, <rect(855, 200, 65, 25)>, <rect(920, 200, 65, 25)>]
floor_mainarray=[(30, 994, 994), (10, 850, 964), (10, 710, 300), (600, 710, 400), (200, 540, 550), (10, 350, 250), (370, 350, 300), (750, 350, 300), (10, 200, 964)]
border_array=[<rect(0, 0, 30, 30)>, <rect(994, 0, 30, 30)>, <rect(0, 30, 30, 30)>, <rect(994, 30, 30, 30)>, <rect(0, 60, 30, 30)>, <rect(994, 60, 30, 30)>, <rect(0, 90, 30, 30)>, <rect(994, 90, 30, 30)>, <rect(0, 120, 30, 30)>, <rect(994, 120, 30, 30)>, <rect(0, 150, 30, 30)>, <rect(994, 150, 30, 30)>, <rect(0, 180, 30, 30)>, <rect(994, 180, 30, 30)>, <rect(0, 210, 30, 30)>, <rect(994, 210, 30, 30)>, <rect(0, 240, 30, 30)>, <rect(994, 240, 30, 30)>, <rect(0, 270, 30, 30)>, <rect(994, 270, 30, 30)>, <rect(0, 300, 30, 30)>, <rect(994, 300, 30, 30)>, <rect(0, 330, 30, 30)>, <rect(994, 330, 30, 30)>, <rect(0, 360, 30, 30)>, <rect(994, 360, 30, 30)>, <rect(0, 390, 30, 30)>, <rect(994, 390, 30, 30)>, <rect(0, 420, 30, 30)>, <rect(994, 420, 30, 30)>, <rect(0, 450, 30, 30)>, <rect(994, 450, 30, 30)>, <rect(0, 480, 30, 30)>, <rect(994, 480, 30, 30)>, <rect(0, 510, 30, 30)>, <rect(994, 510, 30, 30)>, <rect(0, 540, 30, 30)>, <rect(994, 540, 30, 30)>, <rect(0, 570, 30, 30)>, <rect(994, 570, 30, 30)>, <rect(0, 600, 30, 30)>, <rect(994, 600, 30, 30)>, <rect(0, 630, 30, 30)>, <rect(994, 630, 30, 30)>, <rect(0, 660, 30, 30)>, <rect(994, 660, 30, 30)>, <rect(0, 690, 30, 30)>, <rect(994, 690, 30, 30)>, <rect(0, 720, 30, 30)>, <rect(994, 720, 30, 30)>, <rect(0, 750, 30, 30)>, <rect(994, 750, 30, 30)>, <rect(0, 780, 30, 30)>, <rect(994, 780, 30, 30)>, <rect(0, 810, 30, 30)>, <rect(994, 810, 30, 30)>, <rect(0, 840, 30, 30)>, <rect(994, 840, 30, 30)>, <rect(0, 870, 30, 30)>, <rect(994, 870, 30, 30)>, <rect(0, 900, 30, 30)>, <rect(994, 900, 30, 30)>, <rect(0, 930, 30, 30)>, <rect(994, 930, 30, 30)>, <rect(0, 960, 30, 30)>, <rect(994, 960, 30, 30)>, <rect(0, 990, 30, 30)>, <rect(994, 990, 30, 30)>, <rect(0, 1020, 30, 30)>, <rect(994, 1020, 30, 30)>, <rect(0, 0, 30, 30)>, <rect(0, 994, 30, 30)>, <rect(30, 0, 30, 30)>, <rect(30, 994, 30, 30)>, <rect(60, 0, 30, 30)>, <rect(60, 994, 30, 30)>, <rect(90, 0, 30, 30)>, <rect(90, 994, 30, 30)>, <rect(120, 0, 30, 30)>, <rect(120, 994, 30, 30)>, <rect(150, 0, 30, 30)>, <rect(150, 994, 30, 30)>, <rect(180, 0, 30, 30)>, <rect(180, 994, 30, 30)>, <rect(210, 0, 30, 30)>, <rect(210, 994, 30, 30)>, <rect(240, 0, 30, 30)>, <rect(240, 994, 30, 30)>, <rect(270, 0, 30, 30)>, <rect(270, 994, 30, 30)>, <rect(300, 0, 30, 30)>, <rect(300, 994, 30, 30)>, <rect(330, 0, 30, 30)>, <rect(330, 994, 30, 30)>, <rect(360, 0, 30, 30)>, <rect(360, 994, 30, 30)>, <rect(390, 0, 30, 30)>, <rect(390, 994, 30, 30)>, <rect(420, 0, 30, 30)>, <rect(420, 994, 30, 30)>, <rect(450, 0, 30, 30)>, <rect(450, 994, 30, 30)>, <rect(480, 0, 30, 30)>, <rect(480, 994, 30, 30)>, <rect(510, 0, 30, 30)>, <rect(510, 994, 30, 30)>, <rect(540, 0, 30, 30)>, <rect(540, 994, 30, 30)>, <rect(570, 0, 30, 30)>, <rect(570, 994, 30, 30)>, <rect(600, 0, 30, 30)>, <rect(600, 994, 30, 30)>, <rect(630, 0, 30, 30)>, <rect(630, 994, 30, 30)>, <rect(660, 0, 30, 30)>, <rect(660, 994, 30, 30)>, <rect(690, 0, 30, 30)>, <rect(690, 994, 30, 30)>, <rect(720, 0, 30, 30)>, <rect(720, 994, 30, 30)>, <rect(750, 0, 30, 30)>, <rect(750, 994, 30, 30)>, <rect(780, 0, 30, 30)>, <rect(780, 994, 30, 30)>, <rect(810, 0, 30, 30)>, <rect(810, 994, 30, 30)>, <rect(840, 0, 30, 30)>, <rect(840, 994, 30, 30)>, <rect(870, 0, 30, 30)>, <rect(870, 994, 30, 30)>, <rect(900, 0, 30, 30)>, <rect(900, 994, 30, 30)>, <rect(930, 0, 30, 30)>, <rect(930, 994, 30, 30)>, <rect(960, 0, 30, 30)>, <rect(960, 994, 30, 30)>, <rect(990, 0, 30, 30)>, <rect(990, 994, 30, 30)>, <rect(1020, 0, 30, 30)>, <rect(1020, 994, 30, 30)>]
class mario_tests()::
    def mario_init_test():
        mario=player(12,4)
        assert mario.startx == 30 
        and mario.starty == 955 
        and mario.rect== pygame.Rect(30,900,25,39)
        assert mario.on_the_floor == 1

    def mario_inside_ladder():
        mario=player(12,4)
        mario.y-=2
	mario.adjust_irregularities(floor_mainarray)
	assert mario.on_the_floor == 1
	mario.x=693
	mario.y=853
	mario.ladder_set(ladder_array)
	assert mario.ladder == 1
	mario.check_on_the_floor(floor_mainarray)
	assert mario.on_the_floor == 0
	

