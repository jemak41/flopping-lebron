import pygame
from pygame.locals import *
import random
import os
from sys import exit
from os import path
from flop import *
from define import *

def game_over():

    clock.tick(50)
    pygame.mixer.music.stop()
    game = myfont.render("GAME OVER!", False,(255,255,255))
    flop = myfont.render("YOU FLOPPED", False,(255,255,255))
    #background = pygame.image.load("lebron flop.jpg").convert()

    gameover_sound.play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        games.update()
        screen.fill((0,0,0))
        #screen.blit(background, (50, 0))
        games.draw(screen)
        screen.blit(game, (55,10))

        screen.blit(flop, (50, SCREENSIZE[1] - 80))
        pygame.display.flip()

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
                player.image = pygame.image.load(os.path.join(img_folder, "crying bron-2.jpg")).convert()
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
    update_pipe()

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