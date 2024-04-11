import pygame, sys

pygame.init()
pygame.mouse.set_visible(False)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y,speed_x,speed_y):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.pos_x = pos_x
        self.pos_y = pos_y
        # print(speed_x, speed_y)
        self.speed_x = speed_x * 0.1
        self.speed_y = speed_y * 0.1

         

    def update(self):
        #self.speed_y += 1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right >= screen_width:
            self.speed_x *= -1
        if self.rect.bottom >= screen_height:
            self.speed_y *= -1
        if self.rect.x <= -200:
            self.kill()
        

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound(r"Python\roblox-oof-gamespecifications.com_-1.mp3")

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        self.gunshot.play()

    def create_bullet(self):
        mouse_rel = pygame.mouse.get_rel()
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],mouse_rel[0],mouse_rel[1])

        

clock = pygame.time.Clock()


screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

background = (210,210,255)


crosshair = Crosshair("Python\crosshair_red_small.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

bullet_group = pygame.sprite.Group()


while True:
    (x,y) = pygame.mouse.get_pos()

    screen.fill(background)
    

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
            bullet_group.add(crosshair.create_bullet())

    crosshair_group.draw(screen)
    bullet_group.draw(screen)

    pygame.draw.rect(screen,(0,0,0),(0,screen_height-100,50,100))
    pygame.draw.ellipse(screen,(0,0,0),(0,screen_height-120,150,50))

    bullet_group.update()
    crosshair_group.update()
    pygame.display.flip()
    clock.tick(60)