import pygame, sys, random, math

class Rectangelen(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y, rel_x,rel_y, R,G,B, sidelength):
        super().__init__()
        self.image = pygame.Surface((sidelength,sidelength))
        self.image.fill((R,G,B))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.rel_x = rel_x
        self.rel_y = rel_y

    def collide(self, spriteGroup):
        collided_sprites = pygame.sprite.spritecollide(self, spriteGroup, False)
        for sprite in collided_sprites:
            if sprite != self:
                if pygame.sprite.collide_rect(self, sprite):
                    if self.rect.right >= sprite.rect.left and self.rel_x > 0:
                        self.rel_x *= -1
                    if self.rect.left <= sprite.rect.right and self.rel_x < 0:
                        self.rel_x *= -1
                    if self.rect.bottom >= sprite.rect.top and self.rel_y > 0:
                        self.rel_y *= -1
                    if self.rect.top <= sprite.rect.bottom and self.rel_y < 0:
                        self.rel_y *= -1

    def update(self):
        self.rect.x += self.rel_x
        self.rect.y += self.rel_y

        self.rel_y += 2

        if self.rect.right >= screen_width and self.rel_x > 0:
            self.rel_x *= -1 
        elif self.rect.top <= 0 and self.rel_y < 0:
            self.rel_y *= -1
        if self.rect.left <= 0 and self.rel_x < 0:
            self.rel_x *= -1 
        if self.rect.bottom >= screen_height and self.rel_y > 0:
            self.rel_y *= -0.9

        # collisions with each other

    

        #if abs(other_rect.top - moving_rect.bottom) < 10 and moving_y > 0 and other_y < 0:
        




""" def bouncing_rect():

    global moving_x, moving_y, other_x, other_y

    pygame.draw.rect(screen, (210,255,210), moving_rect)
    pygame.draw.rect(screen,(255,210,210),other_rect)
    moving_rect.x += moving_x
    moving_rect.y += moving_y
    other_rect.x += other_x
    other_rect.y += other_y

    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        moving_x *= -1 
    if moving_rect.top <= 0 or moving_rect.bottom >= screen_height:
        moving_y *= -1
    if other_rect.right >= screen_width or other_rect.left <= 0:
        other_x *= -1 
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_y *= -1

    # collision with each other

    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < 10 and moving_y > 0 and other_y < 0:
            moving_y *= -1
            other_y *= -1
        if abs(other_rect.bottom - moving_rect.top) < 10 and moving_y < 0 and other_y < 0:
            moving_y *= -1
            other_y *= -1
        if abs(other_rect.right - moving_rect.left) < 10 and moving_x < 0 and other_x > 0:
            moving_x *= -1
            other_x *= -1
        if abs(other_rect.left - moving_rect.right) < 10 and moving_x > 0 and other_x < 0:
            moving_x *= -1
            other_x *= -1 """
        
pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))



Rectangelen_group = pygame.sprite.Group()
for kvad in range(30):
    new_rect = Rectangelen(random.randrange(0,screen_width), random.randrange(0,screen_height),random.randrange(-3,3),random.randrange(-3,3)\
                           ,random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),random.randrange(10,40))
    Rectangelen_group.add(new_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    screen.fill((210,210,255))

    for kvad in Rectangelen_group:
        kvad.collide(Rectangelen_group)

    Rectangelen_group.draw(screen)
    Rectangelen_group.update()

    pygame.display.flip()

    clock.tick(60)

    