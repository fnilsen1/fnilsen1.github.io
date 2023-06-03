import pygame
import sys
import os
import random
import math

pygame.init()
WIDTH, HEIGHT = (800, 600)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

path = os.path.dirname(__file__)

class Entity():
    def __init__(self, x,y,speed_x,speed_y,img, type):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.img = img
        self.type = type
    
    def move(self):
         self.x+=self.speed_x
         self.y+=self.speed_y
         if(self.y<68):
              self.speed_y=-self.speed_y

         if(self.y>532):
              self.speed_y=-self.speed_y

         if(self.x>732):
            self.speed_x=-self.speed_x

         if(self.x<68):
            self.speed_x=-self.speed_x
            
         
    def draw(self):
        WINDOW.blit(self.img, (self.x-68, self.y-68))


    def collision(self):
        for i in entity_list:
            if(math.sqrt((self.x-i.x)**2+(self.y-i.y)**2) <138):
                if(self.type=="stein" and i.type == "saks"):
                    i.img=self.img
                    i.type = self.type

                elif(self.type=="saks" and i.type == "papir"):
                    i.img=self.img
                    i.type = self.type

                elif(self.type=="papir" and i.type == "stein"):
                    i.img=self.img
                    i.type = self.type

                
                
         
        
          


stein_img = pygame.image.load(os.path.join(path, 'Assets', 'stein.png')) #denne fungerer på alle OS
stein_img = pygame.transform.scale(stein_img, (136,136))

saks_img = pygame.image.load(os.path.join(path, 'Assets', 'saks.png')) #denne fungerer på alle OS
saks_img = pygame.transform.scale(saks_img, (136,136))

papir_img = pygame.image.load(os.path.join(path, 'Assets', 'papir.png')) #denne fungerer på alle OS
papir_img = pygame.transform.scale(papir_img, (136,136))
 
#136x136
entity_list = []
def main():
    clock = pygame.time.Clock()
    run = True
    
    type_list = ["stein", "saks","papir"]
    img_list = [stein_img,saks_img,papir_img]
    for i in range(10):
        a = random.randint(68,732)
        b = random.randint(68,532)
        c = random.randint(0,2)
        entity_list.append(Entity(a,b,1,2,img_list[c],type_list[c]))

    stone = Entity(100,100, 2, 4, stein_img, "stein")
    while run:
            clock.tick(60)
            WINDOW.fill((255,255,255))
            for i in entity_list:
                    
                i.move()
                i.collision()
                i.draw()

            # WINDOW.blit(stein_img, (0, 0))





            pygame.display.flip()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                
main()
