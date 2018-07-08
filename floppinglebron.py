import pygame
from pygame.locals import *
import random
import os
from sys import exit
from os import path

pygame.init()
pygame.mixer.init()
SCREENSIZE = 500, 600
top_pipe = random.randint(100, SCREENSIZE[1] - 200)
bottom_pipe = SCREENSIZE[1] - top_pipe - 200

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")

myfont = pygame.font.SysFont("comicsansms", 60)
score = 0

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Lebron Flopping Game")
background = pygame.image.load(os.path.join(img_folder, "BG.png")).convert()
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "crying bron3.jpg")).convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.left = SCREENSIZE[0] / 6
        self.rect.top = SCREENSIZE[1] / 2
        self.y_speed = 5

    def update(self):
        #self.rect.x += 5
        self.rect.y += 3
        keys = pygame.key.get_pressed()


        #Top
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, top_pipe))
        #self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.left = 250
        self.rect.top = 0

    def update(self):
        self.rect.x -= 4
        if self.rect.left < - 50:
            self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
            self.image = pygame.transform.scale(self.image, (50, top_pipe))
            self.rect = self.image.get_rect()
            self.rect.right = SCREENSIZE[0] + 50
            self.rect.top = 0
            global score
            score += 1
            coin_sound.play()

class Pipe2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, top_pipe))
        self.rect = self.image.get_rect()
        self.rect.left = 500
        self.rect.top = 0

    def update(self):
        self.rect.x -= 4
        if self.rect.left < -50:
            self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
            self.image = pygame.transform.scale(self.image, (50, top_pipe))
            self.rect = self.image.get_rect()
            self.rect.right = SCREENSIZE[0] + 50
            self.rect.top = 0
            global score
            score += 1
            coin_sound.play()

#Bottom
class Pipe3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, bottom_pipe))
        self.rect = self.image.get_rect()
        self.rect.left = 250
        self.rect.top = SCREENSIZE[1] - 50

    def update(self):
        self.rect.x -= 4
        if self.rect.left < -50:
            self.rect.right = SCREENSIZE[0] + 50
            self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
            self.image = pygame.transform.scale(self.image, (50, bottom_pipe))
            self.rect.top = SCREENSIZE[1] - bottom_pipe

class Pipe4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, bottom_pipe))
        self.rect = self.image.get_rect()
        self.rect.left = 500
        self.rect.top = SCREENSIZE[1] - 50

    def update(self):
        self.rect.x -= 4
        if self.rect.left < -50:
            self.rect.right = SCREENSIZE[0] + 50
            self.image = pygame.image.load(os.path.join(img_folder, "Barrel.png")).convert()
            self.image = pygame.transform.scale(self.image, (50, bottom_pipe))
            self.rect.top = SCREENSIZE[1] - bottom_pipe

class Over(pygame.sprite.Sprite):
    def __init__(self):
        super(Over, self).__init__()
        self.image = pygame.image.load(os.path.join(img_folder, "crying bron3.jpg")).convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left = SCREENSIZE[0] / 6
        self.rect.top = SCREENSIZE[1] / 2
        self.y_speed = 5
    def update(self):
        self.rect.y += 1
        if self.rect.top > SCREENSIZE[1]:
            self.rect.top = 0

def game_over():

    clock.tick(1)
    pygame.mixer.music.stop()
    game = myfont.render("GAME OVER!", False,(255,255,255))
    flop = myfont.render("YOU FLOPPED", False,(255,255,255))
    background = pygame.image.load("lebron flop.jpg").convert()
    gameover_sound.play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        games.update()
        screen.fill((0,0,0))
        screen.blit(background, (50, 0))
        games.draw(screen)
        screen.blit(game, (55,10))

        screen.blit(flop, (50, SCREENSIZE[1] - 80))
        pygame.display.flip()

#Sounds
jump_sound = pygame.mixer.Sound(path.join(snd_folder, "smb_jump-super.wav"))
jump_sound.set_volume(.5)
coin_sound = pygame.mixer.Sound(path.join(snd_folder, "smb_coin.wav"))
gameover_sound = pygame.mixer.Sound(path.join(snd_folder, "smb_mariodie.wav"))

pygame.mixer.music.load("bgsound.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Sprites
sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
player = Player()
pipe = Pipe()
pipe2 = Pipe2()
pipe3 = Pipe3()
pipe4 = Pipe4()
sprites.add(player, pipe, pipe2, pipe3, pipe4)
pipes.add(pipe)
pipes.add(pipe2)
pipes.add(pipe3)
pipes.add(pipe4)

games = pygame.sprite.Group()
ova = Over()
games.add(ova)

#Game Loop
while True:
    clock.tick(30)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.image = pygame.image.load(os.path.join(img_folder, "crying bron2.jpg")).convert()
                player.image = pygame.transform.scale(player.image, (100, 100))
                player.image.set_colorkey((255, 255, 255))
                player.rect.y -= 30
                jump_sound.play()
        if event.type == KEYUP:
            if event.key == pygame.K_SPACE:
                player.image = pygame.image.load(os.path.join(img_folder, "crying bron3.jpg")).convert()
                player.image = pygame.transform.scale(player.image, (100, 100))
                player.image.set_colorkey((255, 255, 255))

    # Update
    top_pipe = random.randint(100, SCREENSIZE[1] - 300)
    bottom_pipe = SCREENSIZE[1] - top_pipe - 300
    sprites.update()

    hits = pygame.sprite.spritecollide(player, pipes, False)
    if hits:
        game_over()

    # Draw / render
    screen.blit(background,(0,0))
    sprites.draw(screen)

    scores = myfont.render(str(score), False, (255, 255, 255))
    screen.blit(scores, (SCREENSIZE[0] / 2 - 30,10))

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()