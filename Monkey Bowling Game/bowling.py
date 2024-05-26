#Importerer bibliotek
# from tkinter.tix import Balloon
import pygame as pg
from pygame import mixer
import math as m
import time


# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
speed = 1
angle = 90

#Laster inn musikkfilene. (0) er kanalen hvor lyden blir spilt av. Dette er for flere spor samtidig
pg.mixer.music.load("coconut_mall.mp3")
pg.mixer.music.load("monkey_sound.mp3")
pg.mixer.Channel(0).play(pg.mixer.Sound('coconut_mall.mp3'))

#Dette er en klasse med mange attributter. Dette er i stedet for å bruke global variabler
class Game_stats:

    def __init__(self, game_running, runde, pins_knocked, game_list, total_score, points_tmp, true_game_list, frames, counter):

        self.game_running = game_running
        self.runde = runde
        self.pins_knocked = pins_knocked
        self.game_list = game_list
        self.total_score = total_score
        self.points_tmp= points_tmp
        self.true_game_list= true_game_list
        self.frames= frames
        self.counter= counter

#Vi lager et objekt fra klassen Game_stats
game_state = Game_stats(False,0, 0, [], 0,0,[], [],0)


class Ball:
    """Klasse for å representere en ball"""

    def __init__(self, x, y, fart_x, fart_y, radius, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart_x = fart_x
        self.fart_y = fart_y
        self.radius = radius
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, (0, 0, 0),
                       (self.x, self.y), self.radius+2)
        pg.draw.circle(self.vindusobjekt, (255, 69, 0),
                       (self.x, self.y), self.radius)

    def flytt(self):
        """Metode for å flytte ballen"""
        # Sjekker om ballen er utenfor høyre/venstre kant
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= 450):
            self.fart_x = -self.fart_x

        # Flytter ballen
        self.x += self.fart_x
        self.y += -self.fart_y

        if((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.fart_y = -self.fart_y


class Line:
    """Klasse for å representere en linje"""

    def __init__(self, point1, point2):
        """Konstruktør"""
        self.point1 = point1
        self.point2 = point2

    def tegn(self):
        """Metode for å tegne en linje"""
        pg.draw.line(vindu, (0, 0, 0), self.point1, self.point2, 3)


class Pin:
    """Klasse for å representere pins"""

    def __init__(self, x, y, radius, knocked_state, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.radius = radius
        self.knocked_state = knocked_state
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne pins"""
        if(self.knocked_state == True):
            return
        else:
            pg.draw.circle(self.vindusobjekt, (0, 0, 0),
                           (self.x, self.y), self.radius+2)
            pg.draw.circle(self.vindusobjekt, (255, 255, 255),
                           (self.x, self.y), self.radius)

#Denne funksjonen kalkulerer scoren til hver frame
def calculate_frames():
    frames = game_state.true_game_list
    values = game_state.game_list
    count = 0
    the_sum = 0
    the_sum_list = []

    for i in range(len(frames)):
        if not frames[i] == []:
            if not "X" in frames[i] and not "/" in frames[i]:
                the_sum += sum(frames[i])
                count += 2
            elif frames[i][0] == "X":
                try:
                    the_sum += 10+values[count+1]+values[count+2]
                except:
                    pass
                count += 1
            elif "/" in frames[i]:
                count += 1
                try:
                    the_sum += 10+values[count+1]
                except:
                    pass
                count += 1
            the_sum_list.append(the_sum)
    return the_sum_list

#Denne funksjonen fjerner eller setter opp pins
def knocked(pin):
    if(game_state.runde % 2 == 0 and game_state.runde != 0 and game_state.game_running == False):
        pin.knocked_state = False

    if(m.sqrt((abs(pin.x-ball.x))**2+(abs(pin.y-ball.y))**2) <= 50):
        pin.knocked_state = True





def kollisjon():
    
    """Metode for å sjekke om ballen har truffet enden av banen"""
    if(ball.y <= 31):
        ball.x = 227
        ball.y = 630
        ball.fart_x = 0
        ball.fart_y = 0

        
        for k in pins:
            k.tegn()
            knocked(k)
           
            if k.knocked_state:
                game_state.pins_knocked += 1
        
        nested_list=[]
        if(game_state.runde%2==0):
            if(game_state.pins_knocked == 10):
                if(game_state.runde>17):
                    game_state.game_list.append(10)
                  

                    nested_list=[]

                    nested_list.append(["X"])
                    game_state.true_game_list=game_state.true_game_list+(nested_list)

                else:
                    game_state.game_list.append(10)

                    nested_list=[]

                    nested_list.append(["X","-"])
                    game_state.true_game_list=game_state.true_game_list+(nested_list)


            else:
                game_state.points_tmp=game_state.pins_knocked
                nested_list=[]
                
        
                game_state.game_list.append(game_state.points_tmp)
                nested_list.append(game_state.points_tmp)
                game_state.true_game_list.append(nested_list)


                
        else:
            if(game_state.pins_knocked==10):
                
                game_state.game_list.append(game_state.pins_knocked-game_state.points_tmp)

                game_state.true_game_list[-1].append("/")


            
            else:
                game_state.game_list.append(game_state.pins_knocked-game_state.points_tmp)

                game_state.true_game_list[-1].append(game_state.pins_knocked-game_state.points_tmp)


        game_state.runde += 1
        game_state.counter+=1

        game_state.frames=calculate_frames()

        

        
        

        
        if(game_state.pins_knocked == 10 and game_state.runde % 2 != 0):
            pg.mixer.Channel(1).play(pg.mixer.Sound('monkey_sound.mp3'))
            if(game_state.runde<18):

                game_state.runde += 1
  
        game_state.pins_knocked=0
        game_state.game_running = False



# Lager et Ball-objekt
ball = Ball(227, 630, 0, 0, 30, vindu)
pins = [Pin(227, 200, 20, False, vindu), Pin(197, 150, 20, False, vindu), Pin(257, 150, 20, False, vindu), Pin(227, 100, 20, False, vindu),
        Pin(287, 100, 20, False, vindu),
        Pin(167, 100, 20, False, vindu), Pin(197, 50, 20, False, vindu),
        Pin(257, 50, 20, False, vindu), Pin(137, 50, 20,False, vindu), Pin(317, 50, 20, False, vindu)
        ]
line = Line((227, 630), (227, 500))

#Vi laster inn, skalerer og viser bilder
monke = pg.image.load('monke.png')
score = pg.image.load('bowling_score.png')
score = pg.transform.scale(score, (820, 100))
mittBilde = pg.image.load('lane.png')
mittBilde = pg.transform.scale(mittBilde, (450, 720))

# Gjenta helt til brukeren lukker vinduet
fortsett = True


while fortsett:


    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:

                speed -= 1

                if(speed == 0):
                    speed += 1
            if event.key == pg.K_UP:
                speed += 1

                if(speed == 16):
                    speed -= 1

            if event.key == pg.K_RIGHT:
                angle -= 10
                line.point2 = (227+130*m.cos(m.radians(angle)),
                               (630-130*m.sin(m.radians(angle))))

                if(angle == 0):
                    angle += 10
                    line.point2 = (227+130*m.cos(m.radians(angle)),
                                   (630-130*m.sin(m.radians(angle))))

            if event.key == pg.K_LEFT:
                angle += 10
                line.point2 = (227+130*m.cos(m.radians(angle)),
                               (630-130*m.sin(m.radians(angle))))

                if(angle == 180):
                    angle -= 10
                    line.point2 = (227+130*m.cos(m.radians(angle)),
                                   (630-130*m.sin(m.radians(angle))))

            if event.key == pg.K_SPACE:
              
                speed_x = speed*m.cos(m.radians(angle))
                speed_y = speed*m.sin(m.radians(angle))
                ball = Ball(227, 630, speed_x, speed_y, 30, vindu)

                game_state.game_running = True

    # Farger bakgrunnen lyseblå
    vindu.fill((171, 196, 255))

    vindu.blit(mittBilde, (0, 0))
    vindu.blit(monke, (684, 360))
    vindu.blit(score, (455, 10))

    # Tegner og flytter ballen

    for i in pins:
        i.tegn()
        knocked(i)

    ball.tegn()
    line.tegn()
    kollisjon()
    ball.flytt()

    #Vi definerer font, renderer tekst og tegner teksten i vinduet
    pg.font.init()
    my_font = pg.font.SysFont('Comic Saxns MS', 30)
    power_text = my_font.render(f"POWAAH: {speed}", False, (0, 0, 0))
    vinkel_text = my_font.render(f"Vinkel: {angle}°", False, (0, 0, 0))
    intro = my_font.render("Bruk pilene", False, (0, 0, 0))
    vindu.blit(vinkel_text, (500, 550))
    vindu.blit(power_text, (500, 500))
    vindu.blit(intro, (500, 600))


    #X-koordinatene til scores
    forste_x=432
    subscore_x=474

    #For loop som tegner opp scores
    for x in range(len(game_state.true_game_list)):
        for y in range(len(game_state.true_game_list[x])):
            tekst_rute = my_font.render(f"{game_state.true_game_list[x][y]}", False, (0, 0, 0))
            forste_x+=34

            vindu.blit(tekst_rute, (forste_x, 60))

    for i in range(len(game_state.frames)):
            tekst_rute = my_font.render(f"{game_state.frames[i]}", False, (0, 0, 0))

            vindu.blit(tekst_rute, (subscore_x, 90))
            subscore_x+=70
    try:
        #Starter spillet på nytt 
        if(game_state.runde>20 or (game_state.true_game_list[9][0]!="X" and game_state.true_game_list[9][1]!="/")):
        
            ball.x=227
            ball.y=630
            my_font = pg.font.SysFont('Comic Saxns MS', 100)
            ny_runde = my_font.render("Ny runde starter", False, (0, 0, 0))
            vindu.blit(ny_runde, (300, 400))
            pg.draw.rect(vindu, (171, 196, 255), pg.Rect(1170, 0, 200, 200))
            pg.display.flip()
            time.sleep(5)
            game_state = Game_stats(False,0, 0, [], 0,0,[], [],0)
            ball = Ball(227, 630, 0, 0, 30, vindu)
            pins = [Pin(227, 200, 20, False, vindu), Pin(197, 150, 20, False, vindu), Pin(257, 150, 20, False, vindu), Pin(227, 100, 20, False, vindu),
            Pin(287, 100, 20, False, vindu),
            Pin(167, 100, 20, False, vindu), Pin(197, 50, 20, False, vindu),
            Pin(257, 50, 20, False, vindu), Pin(137, 50, 20,False, vindu), Pin(317, 50, 20, False, vindu)
            ]
            line = Line((227, 630), (227, 500))
            angle = 90
  
    except:
        pass
            

    pg.draw.rect(vindu, (171, 196, 255), pg.Rect(1170, 0, 200, 200))
    
    
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
