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
left_player = player.Player(30, "input", width, height)
right_player = player.Player(width - 30 - 25, "ai", width, height)
pong_ball.p1 = left_player
pong_ball.p2 = right_player
right_player.ball = pong_ball

clock = pygame.time.Clock()

masses = []
planet = mass.Mass(np.array([width / 2, height / 2]), (0, 0), 30, size)
planet.mass = 0.5
print(planet.mass)
masses.append(planet)
ball = pong_ball

def transition():
    if gamestate == "NEW":
        return
    global ball
    global gamestate
    ball = mass.Mass(np.array([ball.x, ball.y]), (ball.dir_x * ball.speed, \
        ball.dir_y * ball.speed), 10, size)
    ball.mass = 3
    masses.append(ball)

    gamestate = "NEW"
    print(ball.mass)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                transition()
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
        right_player.update(dt)
        pong_ball.update(dt)

    elif gamestate == "TRANSITION":
        pass
    elif gamestate == "NEW":
        planet.draw(screen)
        ball.update(dt, masses)
        ball.apply_move(dt)

        DIVISOR = 300
        for i in range(0, DIVISOR):
            ddt = dt / DIVISOR
            for mass in masses:
                mass.update(ddt, masses)

            for mass in masses:
                mass.apply_move(ddt)


    """
    Drawing
    """
    screen.fill(black)

    if gamestate == "PONG":
        left_player.draw(screen)
        right_player.draw(screen)
        pong_ball.draw(screen)

    elif gamestate == "TRANSITION":
        pass
    elif gamestate == "NEW":
        planet.draw(screen)
        ball.draw(screen)
        pass

    pygame.display.flip()
