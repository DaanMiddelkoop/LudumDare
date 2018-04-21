import pygame

class Ball(object):
    def __init__(self, x, y, speed, dir_x, dir_y, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.p1 = None
        self.p2 = None
        self.width = width
        self.height = height
        self.collision_width = 25
        self.collision_height = 25

    def update(self, dt):
        if (Ball.collision_check(self.x, self.y, self.collision_width, self.collision_height,
                self.p1.x, self.p1.y, self.p1.collision_width, self.p1.collision_height)):
            self.dir_x = abs(self.dir_x)
            self.p1.collision_height -= 25

        if (Ball.collision_check(self.x, self.y, self.collision_width, self.collision_height,
                self.p2.x, self.p2.y, self.p2.collision_width, self.p2.collision_height)):
            self.dir_x = -abs(self.dir_x)
            self.p2.collision_height -= 25

        if self.x < 0:
            self.dir_x = abs(self.dir_x)

        if self.x - self.collision_width / 2 > self.width:
            self.dir_x = -abs(self.dir_x)

        if self.y < 0:
            self.dir_y = abs(self.dir_y)

        if self.y + self.collision_height / 2 > self.height:
            self.dir_y = -abs(self.dir_y)

        self.x += self.dir_x * self.speed * dt
        self.y += self.dir_y * self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
                pygame.Rect(self.x - self.collision_width / 2, self.y - self.collision_height / 2, self.collision_width, self.collision_height))

    @staticmethod
    def collision_check(x1, y1, w1, h1, x2, y2, w2, h2):
        rect1 = pygame.Rect(x1 - w1 / 2, y1 - h1 / 2, w1, h1)
        rect2 = pygame.Rect(x2 - w2 / 2, y2 - h2 / 2, w2, h2)
        return rect1.colliderect(rect2)
