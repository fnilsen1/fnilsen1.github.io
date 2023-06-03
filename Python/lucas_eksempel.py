# list = [3,2,7,10,1,3,9]
# for i in range(len(list)-1):
#     for j in range(len(list)-1):
#         if(list[j]>list[j+1]):
#             a=list[j]
#             list[j]=list[j+1]
#             list[j+1]=a

# print(list)

import pygame, sys, random
class Crosshair(pygame.sprite.Sprite):
    def init(self, picture_path):
        super().init()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("Pong\score.ogg")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def init(self, picture_path, pos_x,pos_y):
        super().init()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.image = pygame.transform.scale(Anne,(50,200))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load(r"Crosshair\shooting-gallery-pack\PNG\Stall\bg_green.png")
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mouse.set_visible(False)

crosshair = Crosshair("Crosshair\shooting-gallery-pack\PNG\HUD\crosshair_blue_small.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)




Anne = pygame.image.load("Crosshair\AnneFrank.png")
mini_Anne = pygame.transform.scale(Anne,(50,200))

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target(mini_Anne,random.randrange(0,screen_width),random.randrange(0,screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)