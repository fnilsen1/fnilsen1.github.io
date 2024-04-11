
import pygame




pygame.init()

VINDU_BREDDE = 1280
VINDU_HOYDE = 720
vindu = pygame.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
    """Klasse for å representere en ball"""

    def __init__(self, x, y, fart_x, fart_y, radius,  masse):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart_x = fart_x
        self.fart_y = fart_y
        self.radius = radius
        self.masse = masse

    def tegn(self):
        """Metode for å tegne ballen"""
        pygame.draw.circle(self.vindusobjekt, (0, 0, 0),
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


fortsett = True

while fortsett:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False

    vindu.fill((171, 196, 255))
    


    pygame.display.flip()

# Avslutter pygame
pygame.quit()
