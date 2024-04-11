#importerer bibliotek
import pygame
import os
import sys

#initialiserer pygame sammen med lyder og fonts
pygame.init()
pygame.mixer.init()
pygame.font.init()

class Ship:
  """
  En klasse som representerer et romskip
  ...
  Attributter
  -----------
  x : int
    x-posisjonen til romskipet
  y : int
    y-posisjonen til romskipet
  velocity_x : int
    hastigheten til romskipet i x-retning
  velocity_y : int
    hastigheten til romskipet i y-retning
  health : int
    heltall som representerer hvor mange liv man har
  bullet_width : int
    bredden på kulene
  bullet_height : int
    høyden på kulene
  ship_img : Surface
    spriten til skipet

  Metoder
  -------
  mover_player()
    Endrer koordinatene til skipet
  draw()
    Tegner skipet
  """
  def __init__(self, x, y, velocity_x, velocity_y, health, bullet_width, bullet_height, ship_img):
    """
    Konstruerer alle de nødvendige attributtene for et ship-objekt

    Parametere
    ----------
        x : int
            x-posisjonen til romskipet
        y : int
            y-posisjonen til romskipet
        velocity_x : int
            hastigheten til romskipet i x-retning
        velocity_y : int
            hastigheten til romskipet i y-retning
        health : int
            heltall som representerer hvor mange liv man har    
        bullet_width : int
            bredden på kulene
        bullet_height : int
            høyden på kulene
        ship_img : Surface
            spriten til skipet    
    """
    self.x=x
    self.y=y
    self.velocity_x=velocity_x
    self.velocity_y=velocity_y
    self.health=health
    self.bullet_width = bullet_width
    self.bullet_height = bullet_height
    self.ship_img = ship_img


  def move_player(self):
    """
    Endrer koordinatene til skipet og skifter fartsretningen

    Parametere
    ----------
    None

    Returnerer
    ----------
    None
    """

    keys_pressed = pygame.key.get_pressed()
    #opp
    if keys_pressed[pygame.K_w] and self.y > 0:                               
        self.y -= self.velocity_y
    elif self.y < 0:
        self.y = 0    
    #ned
    if keys_pressed[pygame.K_s] and self.y < HEIGHT - SPACESHIP_HEIGHT*1.4:   
        self.y += self.velocity_y
    elif self.y > HEIGHT - SPACESHIP_HEIGHT*1.4:
        self.y = HEIGHT - SPACESHIP_HEIGHT*1.4 
    #venstre
    if keys_pressed[pygame.K_a] and self.x > SPACESHIP_WIDTH/4:                              
        self.x -= self.velocity_x
    #høyre
    if keys_pressed[pygame.K_d] and self.x < WIDTH/2 - SPACESHIP_WIDTH-27:        
        self.x += self.velocity_x

  def draw(self):
    """
    Tegner skipet på skjermen ved gitte koordinater og bilde   
    
    Parametere
    ----------
    None
    
    Returnerer
    ----------
    None     
    """
    #Tegner et skip på skjermen ved gitte koordinater
    WINDOW.blit(self.ship_img, (self.x, self.y))



class Bot(Ship):
  """
  Klasse som representerer bot-skipet og arver fra klassen Ship
  ...

  Attributter
  -----------
  x : int
    x-posisjonen til romskipet
  y : int
    y-posisjonen til romskipet
  velocity_x : int
    hastigheten til romskipet i x-retning
  velocity_y : int
    hastigheten til romskipet i y-retning
  health : int
    heltall som representerer hvor mange liv man har
  bullet_width : int
    bredden på kulene
  bullet_height : int
    høyden på kulene
  ship_img : Surface
    spriten til skipet

  Metoder
  -------
  draw()
    Tegner bot-skipet på skjermen ved gitte koordinater og bilde
  move()
    Endrer koordinatene og retningen til bot-skipet

  """  
  def __init__(self, x, y, velocity_x, velocity_y, health, bullet_width, bullet_height, ship_img):
    """
    Konstruerer alle de nødvendige attributtene for et bot-objekt

    Parametere
    ----------
    x : int
        x-posisjonen til romskipet
    y : int
        y-posisjonen til romskipet
    velocity_x : int
        hastigheten til romskipet i x-retning
    velocity_y : int
        hastigheten til romskipet i y-retning
    health : int
        heltall som representerer hvor mange liv man har
    scout_bullet_width : int
        bredden på kulene
    scout_bullet_height : int
        høyden på kulene
    """
    #Arver fra klassen Ship
    super().__init__(x, y, velocity_x, velocity_y, health,bullet_width, bullet_height, ship_img)

  def move(self):
    """
    Flytter på bot-skipet ved å endre koordinatene og retningen i x- og y-retning

    Parametere
    ----------
    None

    Returnerer
    ----------
    None     
    """

    #Gjør at skipet går opp og ned samtidig som at det går til høyre og venstre
    self.x += self.velocity_x
    self.y+= self.velocity_y
    if(self.y < 0 or self.y > HEIGHT - SPACESHIP_HEIGHT*1.3):
        self.velocity_y=-self.velocity_y
    if(self.x < WIDTH/2+SPACESHIP_WIDTH/2 or self.x > WIDTH-SPACESHIP_WIDTH):
        self.velocity_x=-self.velocity_x

class Button():
    """
    En klasse som representerer en knapp
    ...
    Attributter
    -----------
    x : int
        x-posisjonen til hjørnet øverst til venstre
    y : int
        y-posisjonen til hjørnet øverst til venstre
    image : Surface

    scale: int
        Faktor som skalerer størrelsen på knappen
    
    Metoder
    -------
    draw()
        Tegner knappen og returnerer boolsk variabel
    """    
    def __init__(self, x, y, image, scale):

        """
        Konstruerer alle de nødvendige attributtene for et Button-objekt

        Parametere
        ----------
        x : int
            x-posisjonen til hjørnet øverst til venstre
        y : int
            y-posisjonen til hjørnet øverst til venstre
        image : Surface
            bildet av knappen
        scale: int
            Faktor som skalerer størrelsen på knappen
        """
        #Finner bredden og høyden til bildet av knappen
        width = image.get_width()
        height = image.get_height()
        #Skalerer bildet av knappen
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        #Ser på rektangelet rundt bildet og definerer topleft-koordinatene
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #Knappen skal ikke gjøre noe før den blir trykket på
        self.clicked = False

    def draw(self):
        """  
        Tegner knappen og returnerer boolsk variabel

        Parametere
        ----------
        None

        Returnerer
        ----------
        bool
        """   
        #Knappen har ikke blitt trykket på
        action = False

        #Finner posisjonen til musa
        pos = pygame.mouse.get_pos()

        #Sjekker om musa er over knappen og om den blir trykket på
        if self.rect.collidepoint(pos):
 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                              
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        
        #Returnerer en boolsk variabel
        return action


class Game_info():
    """
    Klasse som representerer game info
    ...

    Attributter
    -----------
    bullets_list_player : list
        liste med bullet-objektene til spilleren
    bullets_list_ai : list
        liste med bullet-objektene til boten
    max_bullets : int
        maks antall kuler man kan ha i lista samtidig
    framecounter : int
        et tall som oppdateres hver nye frame i while-loopen
       

    Metoder
    -------
    None
    """   
    def __init__(self, bullets_list_player, bullets_list_ai, max_bullets, framecounter):
        """
        Konstruerer alle de nødvendige attributtene for et gameinfo-objekt

        Parametere
        ----------
        bullets_list_player : list
            liste med bullet-objektene til spilleren
        bullets_list_ai : list
            liste med bullet-objektene til boten
        max_bullets : int
            maks antall kuler man kan ha i lista samtidig
        framecounter : int
            et tall som oppdateres for hver nye frame i while-loopen
        
        """
    
        self.bullets_list_ai = bullets_list_ai
        self.max_bullets = max_bullets
        self.framecounter = framecounter
        self.bullets_list_player = bullets_list_player
           
#Lager et objekt med klassen Game_info
stats = Game_info([],[],3, 0)

#Masse globale konstanter som alle er relaterte til å tegne opp vinduet og bilder:

#farger
WHITE = (255,255,255)
BLACK = (0,0,0)

#spaceship dimensjoner
WIDTH, HEIGHT = (800, 600)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (50,40)

#Setter bredden og høyden til vinduet lik det vi har valgt
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#Setter caption
pygame.display.set_caption("Plane Duel")
#Vi finner pathen på din maskin som kan brukes til å hente bilder
path = os.path.dirname(__file__)

#Henter surfaces/bilder
SCOUT_IMAGE = pygame.image.load(os.path.join(path, 'Assets', 'spaceship_yellow.png')) #denne fungerer på alle OS
SCOUT_SHIP = pygame.transform.rotate(pygame.transform.scale(SCOUT_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

HEAVY_IMAGE= pygame.image.load(os.path.join(path, 'Assets', 'heavy_ship.png')) #denne fungerer på alle OS
HEAVY_SHIP = pygame.transform.rotate(pygame.transform.scale(HEAVY_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

BOT_IMAGE = pygame.image.load(os.path.join(path, 'Assets', 'spaceship_red.png')) #denne fungerer på alle OS
BOT_SHIP = pygame.transform.rotate(pygame.transform.scale(BOT_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),-90)
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(path, 'Assets', 'space.jpg')), (WIDTH, HEIGHT))

#fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)


def draw_window(player,bot,player_rect,bot_rect, ship_type):
    """  
    Oppdaterer det som blir tegnet på skjermen

        Parametere
        ----------
        player : Ship
            Objektet til player-skipet
        bot : Bot
            Objektet til bot-skipet
        player_rect : pygame.Rect
            Hitbox til spiller
        bot_rect : pygame.Rect
            Hitbox til bot
        ship_type : str
            Hvilken type skipet er (scout/heavy)
        Returnerer
        ----------
        None
    """  
    #Kantutjevning på teksten som skal gi et inntrykk av større oppløsning
    anti_aliasing = True
    #Offset til teksten
    offset = 10
    #Renderer health-tekst
    bot_health_text = HEALTH_FONT.render(f"Health: {bot.health}", anti_aliasing, WHITE)
    player_health_text = HEALTH_FONT.render(f"Health: {player.health}", anti_aliasing, WHITE)
  
    #Tegner bakgrunn og player/bot health tekst
    WINDOW.blit(BACKGROUND_IMAGE, (0,0))
    WINDOW.blit(bot_health_text, (WIDTH - bot_health_text.get_width() - offset, offset))
    WINDOW.blit(player_health_text, (offset,offset))

    #Oppdaterer posisjonen til bot og spiller og tegner dem opp på nytt
    player.move_player()
    bot.move()
    player.draw()
    bot.draw()

    #Lager et gjennomsiktig rektangel og tegner det på midten av skjermen
    s = pygame.Surface((50,HEIGHT))  
    s.set_alpha(128)                
    s.fill((255,255,255))           
    WINDOW.blit(s, (WIDTH/2-25,0))

    #Kjører funksjon som oppdaterer posisjonen til bullets
    bullets(player, bot, player_rect, bot_rect, ship_type)
    #Oppdaterer alt innholdet på skjermen
    pygame.display.flip()


def menu():
  """  
  Tegner startmenyen   

  Parametere
  ----------
  Nonee
  
  Returnerer
  ----------
  str
  """   
  #Henter bilder fra Assets-mappen
  logo_img = pygame.image.load(os.path.join(path, 'Assets', 'space_logo.png')).convert_alpha()
  scout_img = pygame.image.load(os.path.join(path, 'Assets', 'scout.png')).convert_alpha()
  heavy_img = pygame.image.load(os.path.join(path, 'Assets', 'heavy.png')).convert_alpha()
  exit_img = pygame.image.load(os.path.join(path, 'Assets', 'exit.png')).convert_alpha()

  #Mellomrom mellom knappene
  offset = 100

  #Lager objekter av klassen Button
  logo_button = Button(WIDTH/2-250,offset,logo_img, 0.5)
  scout_button = Button(WIDTH/2-offset,offset*2,scout_img, 0.5)
  heavy_button = Button(WIDTH/2-offset,offset*3,heavy_img, 0.5)
  exit_button = Button(WIDTH/2-offset,offset*4,exit_img, 0.5)

  run = True
  #Game-loop
  while run:
    #Gjør hele vinduet sort
    WINDOW.fill(BLACK)

    #Tegner opp logoen til spillet
    logo_button.draw()

    #Hvis scout_button.draw() returnerer True, så returneres "scout"
    if scout_button.draw():
      return("scout")

    elif heavy_button.draw():
      #breaker while-loopen
      break

    elif exit_button.draw():
      #Lukker vinduet hvis man klikker på exit-knappen
      sys.exit()

    #Oppdaterer alt innholdet 
    pygame.display.flip()

    #Går ut av programmet hvis man x-er ut
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()


def main():
  """  
  Startfunksjon som kjører de andre funksjonene
  Inneholder hovedgameloopen
  
  Parametere
  ----------
  None
  
  Returnerer
  ----------
  None
  """  
  #menu returnerer enten scout eller ingenting
  ship_type = menu()
  
  #Du har valgt scout
  if ship_type == "scout": 
     #Lager et objekt av klassen Ship
     player = Ship(100,300,10,10, 3, 10, 4, SCOUT_SHIP)

  #Du har valgt heavy
  else:
     #Lager et objekt av klassen Ship
     player = Ship(100,300,4,4, 4, 18, 8, HEAVY_SHIP)
     
  #Lager et objekt av klassen Bot
  bot = Bot(700,300,5,5, 3, 10, 4, SCOUT_SHIP)

  #Lager et rektangel rundt bildene (hitbox)
  player_rect = pygame.Rect(100,300, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
  bot_rect = pygame.Rect(700,300, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
  
  #Game-loopen får 60 FPS
  clock = pygame.time.Clock()
  FPS = 60
  run = True
  while run:
    clock.tick(FPS)
    #Teller antall frames
    stats.framecounter += 1
    #Kjører funksjon som tegner opp vindu og skip
    draw_window(player,bot,player_rect,bot_rect, ship_type)

def game_over(tekst):
  """  
  Tegner vinneren sitt navn på skjermen
  
  Parametere
  ----------
  tekst : str
  
  Returnerer
  ----------
  None
  """  
  draw_text = GAME_OVER_FONT.render(tekst, 1, WHITE)
  WINDOW.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2,HEIGHT/2 - draw_text.get_height() / 2))
  pygame.display.flip()
  #Venter 5000 ms og restarter spillet
  pygame.time.delay(5000)
  main()


#Custom events
PLAYER_HIT = pygame.USEREVENT + 1
BOT_HIT = pygame.USEREVENT + 2

#lyd
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join(path, 'Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join(path, 'Assets', 'gun_sound.mp3'))
BULLET_DEATH_SOUND = pygame.mixer.Sound(os.path.join(path, 'Assets', 'hit_sound.mp3'))

def bullets(player, bot, player_rect, bot_rect, ship_type):
    """  
    Lager bullets og endrer posisjonen på bullets til både bot og spiller
    Registrer også om noen har vunnet

    Parametere
    ----------
    player : Ship
        Objektet til player-skipet
    bot : Bot
        Objektet til bot-skipet
    player_rect : pygame.Rect
        Hitbox til spiller
    bot_rect : pygame.Rect
        Hitbox til bot
    ship_type : str
        Hvilken type skipet er (scout/heavy)

    Returnerer
    ----------
    None
    """  

    player_rect.x = player.x
    player_rect.y = player.y
    bot_rect.x = bot.x
    bot_rect.y =bot.y

    #Farten til bullet
    bullet_velocity = 15
    
    #Looper gjennom eventlisten
    for event in pygame.event.get():
        #Hvis man trykker en knapp og har nok bullets tilgjengelig
        if event.type == pygame.KEYDOWN and len(stats.bullets_list_player) < stats.max_bullets:
            #Hvis man trykker Left control
            if event.key == pygame.K_LCTRL:
                #Lager en bullet

                bullet = pygame.Rect(player_rect.x + SPACESHIP_WIDTH/2, player_rect.centery - player.bullet_height/2, player.bullet_width, player.bullet_height)

                #Legger til disse objektene i en bulletliste
                stats.bullets_list_player.append(bullet)

                #Spiller av en lyd når man skyter
                BULLET_FIRE_SOUND.play()
        #Sjekker om man har x-et ut av vinduet
        if event.type == pygame.QUIT:
            sys.exit()

        #Sjekker om vår custom event har skjedd
        if event.type == BOT_HIT:
            BULLET_HIT_SOUND.play()
            #Endrer antall liv hos bot
            bot.health -= 1
            if bot.health <= 0:
                #Death sound
                BULLET_DEATH_SOUND.play()
                #Refresher vinduet og fjerner alle bullets hos begge spillere pga ny runde
                draw_window(player, bot, player_rect, bot_rect, ship_type)
                stats.bullets_list_player = []
                stats.bullets_list_ai = []
                #Tegner "Player WON!" på skjermen
                game_over("Player WON!")
         
        if event.type == PLAYER_HIT:
            BULLET_HIT_SOUND.play()
            #Endrer antall liv hos player
            player.health -= 1
            if player.health <= 0:
                #Death sound
                BULLET_DEATH_SOUND.play()
                #Refresher vinduet og fjerner alle bullets hos begge spillere pga ny runde
                draw_window(player, bot, player_rect, bot_rect, ship_type)
                stats.bullets_list_player = []
                stats.bullets_list_ai = []
                #Tegner "BOT WON!" på skjermen
                game_over("BOT WON!")         
   

    #Endrer hastigheten på alle bullets og sier at eventen skjer
    for bullet in stats.bullets_list_player:
      bullet.x += bullet_velocity
      if bot_rect.colliderect(bullet):
        #Kjører event
        pygame.event.post(pygame.event.Event(BOT_HIT))
        #Fjerner bullets som har truffet motstanderen fra lista
        stats.bullets_list_player.remove(bullet)    
      elif(bullet.x > WIDTH):
        #Fjerner bullets utenfor skjermen fra lista
        stats.bullets_list_player.remove(bullet)  
    
    #Tegner rektangler for alle bullets man har skutt
    for bullet in stats.bullets_list_player:
        pygame.draw.rect(WINDOW, (0,255,0), bullet)

    #Boten skyter hvert sekund som blir hver 60ende frame
    if(stats.framecounter%60==0):
        #Lager nye rektangler for hver bullet og legger det til i lista
        bullet = pygame.Rect(bot_rect.x + SPACESHIP_WIDTH/2, bot_rect.centery - bot.bullet_width/2, bot.bullet_width, bot.bullet_height)
        stats.bullets_list_ai.append(bullet)
        BULLET_FIRE_SOUND.play()

    #Endrer hastigheten på alle bullets og sier at eventen skjer
    for bullet in stats.bullets_list_ai:
        bullet.x -= bullet_velocity
        if player_rect.colliderect(bullet):
            #Kjører event
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            #Fjerner bullets som har truffet motstanderen fra lista
            stats.bullets_list_ai.remove(bullet)    
        elif(bullet.x < 0):
            #Fjerner bullets utenfor skjermen fra lista
            stats.bullets_list_ai.remove(bullet)  
            
        #Tegner rektangler for alle bullets man har skutt
        for bullet in stats.bullets_list_ai:
            pygame.draw.rect(WINDOW, (0,255,0), bullet)


#sikrer at main() ikke blir kjørt hvis en annen fil importerer denne filen.
if __name__ == "__main__":
  main()   
