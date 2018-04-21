

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

    def update(self, dt):
        if (self.p1.x < self.x < self.p1.x + self.p1.collision_width and
                self.p1.y < self.y < self.p1.y + self.p1.collision_height) or self.x < 0 or self.x > self.width:
            self.dir_x = -self.dir_x

        if self.x < 0 or self.x > self.width:
            self.dir_x = -self.dir_x

        if self.y < 0 or self.y > self.height:
            self.dir_y = -self.dir_y

        self.x += self.dir_x * self.speed * dt
        self.y += self.dir_y * self.speed * dt
