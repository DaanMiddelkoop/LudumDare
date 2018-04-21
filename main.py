import sys
import pygame
import player
import mass
import numpy as np

pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0
white = 255, 255, 255
red = 255, 100, 100

screen = pygame.display.set_mode(size)

view = [0, 0]
zoom = 1

gamestate = "NEW"

left_player = player.Player(30, "input")
clock = pygame.time.Clock()

planet = mass.Mass((width / 2, height / 2), (0, 0), 40)
# new_left_player?

def transition():
    global ball


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom *= 1.1
            if event.button == 5:
                zoom /= 1.1

    dt = clock.tick()

    """
    Updates and logic
    """
    mov = pygame.mouse.get_rel()
    if (pygame.mouse.get_pressed()[0]):
        view[0] += mov[0] * 1 / zoom
        view[1] += mov[1] * 1 / zoom

    if gamestate == "PONG":
        left_player.update(dt)
    elif gamestate == "TRANSITION":
        pass
    elif gamestate == "NEW":
        planet.draw(screen)
        pass

    """
    Drawing
    """
    screen.fill(black)

    if gamestate == "PONG":
        left_player.draw(screen)
    elif gamestate == "TRANSITION":
        pass
    elif gamestate == "NEW":
        planet.draw(screen)
        pass

    pygame.display.flip()
