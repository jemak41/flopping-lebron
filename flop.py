import pygame
from pygame.locals import *
import random
import os
from sys import exit
from os import path
from define import *

score = 0
top_pipe = random.randint(100, SCREENSIZE[1] - 300)
bottom_pipe = SCREENSIZE[1] - top_pipe - 300

def update_pipe():
    top_pipe = random.randint(100, SCREENSIZE[1] - 300)
    bottom_pipe = SCREENSIZE[1] - top_pipe - 300

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