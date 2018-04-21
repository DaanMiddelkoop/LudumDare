import sys
import pygame
import player
import ball
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

gamestate = "PONG"

pong_ball = ball.Ball(width / 2, height / 2, 0.3, 0.707, 0.707, width, height)
left_player = player.Player(30, "input")
right_player = player.Player(width - 30, "ai")
pong_ball.p1 = left_player
pong_ball.p2 = right_player

clock = pygame.time.Clock()

planet = mass.Mass((width / 2, height / 2), (0, 0), 10)
# new_left_player?


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
        pong_ball.update(dt)
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
        pong_ball.draw(screen)
    elif gamestate == "TRANSITION":
        pass
    elif gamestate == "NEW":
        planet.draw(screen)
        pass

    pygame.display.flip()
