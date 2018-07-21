import pygame
from pygame.locals import *
import random
import os
from sys import exit
from os import path

pygame.init()
pygame.mixer.init()
SCREENSIZE = 500, 600


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")


myfont = pygame.font.SysFont("comicsansms", 60)

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Lebron Flopping Game")
background = pygame.image.load(os.path.join(img_folder, "BG.png")).convert()
clock = pygame.time.Clock()

jump_sound = pygame.mixer.Sound(path.join(snd_folder, "smb_jump-super.wav"))
jump_sound.set_volume(.5)
coin_sound = pygame.mixer.Sound(path.join(snd_folder, "smb_coin.wav"))
gameover_sound = pygame.mixer.Sound(path.join(snd_folder, "smb_mariodie.wav"))