# python tamplate for a new pygame project
import pygame
from random import randint
from os import path
import math

#dir's in the project
img_dir = path.join(path.dirname(__file__), 'img')
sound_dir = path.join(path.dirname(__file__), 'sound')

WIDTH = 400
HEIGHT = 400
FPS = 64

# define colors (red,green,blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_FOR_TEXT = (242,242,242)
COLOR_FOR_GAME = (150, 20, 30)
COLOR_FOR_OPEN_SCREEN = (40,80,90)
COLOR_FOR_LOSE_SCREEN = (90,5,10)
COLOR_FOR_WIN_SCREEN = (90,5,10)
COLOR_FOR_PLAYERS = (255, 255, 80)

center = (WIDTH / 2, HEIGHT / 2)
players_for_2 = False

font_name = pygame.font.match_font('arial')

#the text of life
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, COLOR_FOR_TEXT)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def game_intro():
    #the openning window
    sound_screen.play()
    screen.fill(COLOR_FOR_OPEN_SCREEN)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_KP1 or pygame.K_KP2:
                    intro = False

        draw_text(screen, "PONG", 70, WIDTH / 2, HEIGHT / 5)
        draw_text(screen, "all you need to do is earn 11 points", 20, WIDTH / 2, HEIGHT / 1.8)
        draw_text(screen, "press SPACE to play and Q to quit", 17, WIDTH / 2, HEIGHT / 1.5)
        draw_text(screen, "for 2 players press 2 for 1 player press 1", 17, WIDTH / 2, HEIGHT / 1.3)
        draw_text(screen, "DO IT ONLY WHILE YOU PLAY THE GAME", 17, WIDTH / 2, HEIGHT / 1.1)
        pygame.display.update()
        clock.tick(FPS)

def game_lose():
    # the game lose screen
    sound_screen.play()
    screen.fill(COLOR_FOR_LOSE_SCREEN)
    lose = True
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        draw_text(screen, "LOSE", 70, WIDTH / 2, HEIGHT / 5)
        draw_text(screen, "press Q to quit", 20, WIDTH / 2, HEIGHT / 1.8)
        pygame.display.update()
        clock.tick(FPS)

def game_win():
    #the game win screen
    sound_screen.play()
    screen.fill(COLOR_FOR_WIN_SCREEN)
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        draw_text(screen, "WIN", 70, WIDTH / 2, HEIGHT / 5)
        draw_text(screen, "press Q to quit", 20, WIDTH / 2, HEIGHT / 1.8)
        pygame.display.update()
        clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    """the player class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,45))
        self.image.fill(COLOR_FOR_PLAYERS)
        self.rect = self.image.get_rect()
        self.rect.x = 0 + 10
        self.rect.y = HEIGHT / 2
        self.speedy = 3
        self.points = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speedy
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speedy

    def update(self):
        self.move()

        #keep the player in the screen
        if (self.rect.y > HEIGHT - 45):
            self.rect.y = HEIGHT - 45
        if (self.rect.y < 0):
            self.rect.y = 0

class Player2(pygame.sprite.Sprite):
    """the player2 class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,45))
        self.image.fill(COLOR_FOR_PLAYERS)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 1.069
        self.rect.y = HEIGHT / 2
        self.points = 0
        self.speedy = 3

    def playermove(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP8]:
            self.rect.y -= self.speedy
        if keys[pygame.K_KP5]:
            self.rect.y += self.speedy

    def AI(self):
        if (ball.rect.x > 0):
            self.rect.y += (ball.rect.y - self.rect.y) * math.pow(float(ball.rect.x) / (WIDTH * 2.5), 2.1)

    def update(self):
        if (players_for_2 == True):
            self.playermove()
        else:
            #try some AI
            self.AI()
        #keep the player in the screen
        if (self.rect.y > HEIGHT - 45):
            self.rect.y = HEIGHT - 45
        if (self.rect.y < 0):
            self.rect.y = 0


class Ball(pygame.sprite.Sprite):
    """thw ball class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill((50, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = randint(2,4)
        self.speedy = randint(2,4)

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def update(self):
        self.move()
        #some new code for the game dont make erorr a / 0
        if ball.rect.y == 0:
            ball.rect.y = 1
        if ball.rect.x == 0:
            ball.rect.x = 1

        if (self.rect.right > WIDTH):
            sound_jump1.play()
            self.speedx = randint(-4,-2)
            player2.points += 1
        if (self.rect.bottom > HEIGHT):
            sound_jump1.play()
            self.speedy = randint(-4,-2)
        if (self.rect.top < 0):
            sound_jump1.play()
            self.speedy = randint(2,4)
        if (self.rect.left < 0):
            sound_jump1.play()
            self.speedx = randint(2,4)
            player.points += 1

class Fast(pygame.sprite.Sprite):
    """the fast class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = randint(50,WIDTH - 50)
        self.rect.y = randint(20, HEIGHT - 20)

pygame.init()
pygame.mixer.init()  # for the sound work

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()

#load the sounds
sound_jump1 = pygame.mixer.Sound(path.join(sound_dir, 'jump_01.wav'))
sound_screen = pygame.mixer.Sound(path.join(sound_dir, 'screen_sound.wav'))

#all the groups and the objects
all_sprites = pygame.sprite.Group()
all_balls = pygame.sprite.Group()
all_players = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_players.add(player)
ball = Ball()
all_sprites.add(ball)
all_balls.add(ball)
player2 = Player2()
all_sprites.add(player2)
all_players.add(player2)


# Game Loop
game_intro()
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP2:
                players_for_2 = True
            if event.key == pygame.K_KP1:
                players_for_2 = False

    # update
    all_sprites.update()

    #the ball tach the player
    hits = pygame.sprite.spritecollide(player, all_balls, False)
    for hit in hits:
        ball.speedx = randint(2,4)
        sound_jump1.play()

    #the ball tach the player2
    hits = pygame.sprite.spritecollide(player2, all_balls, False)
    for hit in hits:
        ball.speedx = randint(-4,-2)
        sound_jump1.play()

    #win or lose
    if (player.points == 11):
        game_lose()
    if (player2.points == 11):
        game_win()

    #the game situation
    if players_for_2 == True:
        game_situation = 'FOR TWO PLAYERS'
    else:
        game_situation = 'FOR ONE PLAYER'


    # Draw / render
    screen.fill((COLOR_FOR_GAME))
    all_sprites.draw(screen)
    draw_text(screen, str(player.points), 20, WIDTH / 5, HEIGHT / 15)
    draw_text(screen, str(player2.points), 20, WIDTH / 1.25, HEIGHT / 15)
    draw_text(screen, game_situation, 20, WIDTH / 2, HEIGHT / 15)

    # after! drawing everything flip to display
    pygame.display.flip()

pygame.quit()