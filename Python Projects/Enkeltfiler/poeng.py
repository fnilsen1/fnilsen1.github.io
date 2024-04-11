import pygame as pg
from pygame import mixer
import math
import time
import random

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:

    def __init__(self, x, y, fart_x, fart_y, radius, vindusobjekt):

        self.x = x
        self.y = y
        self.fart_x = fart_x
        self.fart_y = fart_y
        self.radius = radius
        self.poeng = 0

        self.vindusobjekt = vindusobjekt
        self.move_right = False
        self.move_left = False

    def tegn(self):

        pg.draw.circle(self.vindusobjekt, (0, 0, 0),
                       (self.x, self.y), self.radius+2)
        pg.draw.circle(self.vindusobjekt, (255, 69, 0),
                       (self.x, self.y), self.radius)

    def flytt(self):
        if self.move_right==True:
            self.x += self.fart_x

        if self.move_left==True:
            self.x -= self.fart_x
        
        if self.x+30 >= 1280:
            self.x-=1

        if self.x-30 <= 0:
            self.x+=1



        else:
            self.x += 0

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hit = False

    def tegn(self):
        pg.draw.circle(vindu, (0, 0, 0),
                       (self.x, self.y), 20)
    def flytt(self):
            self.y += 0.2

    def truffet(self):
        if(math.sqrt((ball.y-self.y)**2)<50):
            self.hit = True
            

ball = Ball(640, 680, 1, 0, 30, vindu)
target_list = []
fortsett = True

def flere_baller():
    random_number = random.randint(30, 1250)
    target_list.append(Target(random_number,50))

flere_baller()

last_time = time.time()
while fortsett:
    current_time = time.time()
    if current_time - last_time >= 2:
        flere_baller()
        last_time = current_time
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False


        if event.type == pg.KEYDOWN:
       
            if event.key == pg.K_RIGHT:
                ball.move_right = True

            elif event.key == pg.K_LEFT:
                ball.move_left = True


        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                ball.move_right = False
                
            if event.key == pg.K_LEFT:
                ball.move_left = False

    vindu.fill((171, 196, 255))
    ball.flytt()

    
    for i in target_list:
        i.tegn()
        i.flytt()
        i.truffet()
    ball.tegn()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
