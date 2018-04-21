import pygame

class Player(object):
    def __init__(self, x, strat):
        self.x = x
        self.y = 100
        self.strat = strat
        self.collision_width = 10
        self.collision_height = 100

    def update(self, dt):
        if self.strat == "input":
            if pygame.key.get_pressed()[pygame.K_w]:
                self.y += 0.3 * dt
            if pygame.key.get_pressed()[pygame.K_s]:
                self.y -= 0.3 * dt

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
            pygame.Rect(self.x, self.y, self.collision_width, self.collision_height))
