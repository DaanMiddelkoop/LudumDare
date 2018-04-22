import pygame

class Player(object):
    def __init__(self, x, strat, width, height):
        self.x = x
        self.y = 100
        self.strat = strat
        self.collision_width = 10
        self.collision_height = 300
        self.ball = None
        self.width = width
        self.height = height
        self.button_up = pygame.K_w
        self.button_down = pygame.K_s

    def update(self, dt):
        if self.strat == "input":
            if pygame.key.get_pressed()[self.button_down]:
                self.y += 0.3 * dt
            if pygame.key.get_pressed()[self.button_up]:
                self.y -= 0.3 * dt

        if self.strat == "ai":
            if self.y > self.ball.y:
                self.y -= 0.3 * dt
            else:
                self.y += 0.3 * dt
        if self.y - self.collision_height / 2 < 0:
            self.y = self.collision_height / 2

        if self.y + self.collision_height / 2 > self.height:
            self.y = self.height - self.collision_height / 2

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
            pygame.Rect(self.x - self.collision_width / 2, self.y - self.collision_height / 2, self.collision_width, self.collision_height))
