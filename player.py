import pygame

class Player(object):
    def __init__(self, h_pos, strat):
        self.h_pos = h_pos
        self.v_pos = 100
        self.strat = strat

    def update(self):
        if self.strat == "input":
            if pygame.key.get_pressed()[pygame.K_w]:
                self.v_pos += 1
            if pygame.key.get_pressed()[pygame.K_s]:
                self.v_pos -= 1
        print(self.v_pos)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
            pygame.Rect(self.h_pos, self.v_pos, 10, 100))
