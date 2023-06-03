import pygame as pg

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))
    pg.draw.circle(vindu, (0, 0, 0), (100, 100), 30) 
    pg.draw.circle(vindu, (255, 69, 0), (100, 100), 28) 
    # Oppdaterer alt innholdet i vinduet

    pg.display.flip()

# Avslutter pygame
pg.quit()