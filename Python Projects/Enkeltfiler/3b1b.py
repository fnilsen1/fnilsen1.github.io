import pygame, sys, random, math

class Rectangelen(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y, rel_x,rel_y, RGB, sidelength, mass):
        super().__init__()
        self.image = pygame.Surface((sidelength,sidelength))
        self.image.fill(RGB)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.mass = mass

    def collide(self, spriteGroup):
        collided_sprites = pygame.sprite.spritecollide(self, spriteGroup, False)
        for sprite in collided_sprites:
            if sprite != self:
                if self.rect.colliderect(sprite): 
                    
                    threshhold = 5
                    if abs(sprite.rect.right - self.rect.left) < threshhold:
                        #self.rel_x *= -1
                        self.rel_x = (self.mass - sprite.mass)/(self.mass + sprite.mass)*self.rel_x + 2*sprite.mass/(self.mass + sprite.mass)*sprite.rel_x

                    if abs(sprite.rect.left - self.rect.right) < threshhold:
                        #self.rel_x *= -1
                        self.rel_x = (self.mass - sprite.mass)/(self.mass + sprite.mass)*self.rel_x + 2 * sprite.mass/(self.mass + sprite.mass)*sprite.rel_x 

     

    def update(self):
        self.rect.x += self.rel_x
        self.rect.y += self.rel_y

        if self.rect.right >= screen_width and self.rel_x > 0:
            self.rel_x *= -1 
        if self.rect.left <= 0 and self.rel_x < 0:
            self.rel_x *= -1 


        
pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))


Rectangelen_group = pygame.sprite.Group()


#size, velocity, position, mass
Data = ([100,100],[0,-1.5],[200,500],[10,100])

for kvad in range(2):

    new_rect = Rectangelen(
        Data[2][kvad],
        screen_height -Data[0][kvad]/2,
        Data[1][kvad],
        0,
        (random.randrange(0, 255),
        random.randrange(0, 255),
        random.randrange(0, 255)),
        Data[0][kvad],
        Data[3][kvad])

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

    