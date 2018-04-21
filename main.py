import sys
import pygame
import player

pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0
white = 255, 255, 255
red = 255, 100, 100

screen = pygame.display.set_mode(size)

view = [0, 0]
zoom = 1

gamestate = "PONG"

left_player = player.Player(30, "input")
clock = pygame.time.Clock()


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
        pass

    """
    Drawing
    """
    screen.fill(black)

    left_player.draw(screen)

    pygame.display.flip()
