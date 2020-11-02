import pygame
from pygame.draw import *
from random import randint as ran
from math import sin, cos, atan, pi

from my_color import *

"Version pygame 2.0.0"
pygame.init()
FPS = 60
screen_x, screen_y = 1200, 600
screen = pygame.display.set_mode((screen_x, screen_y))


def score_count():
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(text_1, text_1.get_rect(center=(screen_x // 10, screen_y // 10)))


class Timer:
    def __init__(self, lap):
        self.lap = lap
        self.start_time = pygame.time.get_ticks()

    def time(self):
        return self.start_time + self.lap > pygame.time.get_ticks()


class Ground:
    def __init__(self):
        self.y = 19 * screen_y // 20

    def draw(self):
        line(screen, BLACK, (0, self.y), (screen_x, self.y), 3)


class Cannon:
    def __init__(self, start_side, y, x=screen_x // 25, color=ARMY, width=9):
        self.color = color
        self.start_side = start_side
        self.side = start_side
        self.r = start_side / 2
        self.x = x
        self.y = y - self.r - 2
        self.width = width
        self.side_v = start_side / 75
        self.angle = 0

    def draw(self):
        circle(screen, ARMY, (self.x, self.y), self.r)
        rect(screen, ARMY, (self.x - 2 * self.r, self.y + 1, 4 * self.r, self.r))
        polygon(screen, self.color, [(self.x, self.y),
                                     (self.x + self.side * cos(self.angle), self.y + self.side * sin(self.angle)),
                                     (self.x + self.side * cos(self.angle) + self.width * sin(self.angle),
                                      self.y + self.side * sin(self.angle) - self.width * cos(self.angle)),
                                     (self.x + self.width * sin(self.angle),
                                      self.y - self.width * cos(self.angle))])

    def move(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x - self.x > 0 > mouse_y - self.y:
            self.angle = atan((mouse_y - self.y) / (mouse_x - self.x))

        if pygame.mouse.get_pressed(3)[0]:
            self.side += self.side_v
            if self.side > 1.7 * self.start_side:
                self.side_v = -abs(self.side_v)
            elif self.side < self.start_side:
                self.side_v = abs(self.side_v)

        else:
            self.side = self.start_side


class Bullet:
    def __init__(self, x, y, v, r, g=0.4):
        self.angel = cannon.angle
        self.color = BLACK
        self.x = x
        self.y = y
        self.v = v
        self.vx = v * cos(self.angel)
        self.vy = v * sin(self.angel)
        self.r = r
        self.g = g
        self.tries = 0

    def draw(self):
        if self.vx ** 2 + self.vy ** 2 > cannon.start_side / 12 or self.y < ground.y - 20:
            circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        if self.vx ** 2 + self.vy ** 2 > cannon.start_side / 12 or self.y < ground.y - 20:
            self.x += self.vx
            self.y += self.vy
            self.vy += self.g

        if self.x + self.r > screen_x:
            self.vx = -abs(self.vx) / 2
            self.vy = self.vy * 0.8
            self.x -= 10
        if self.y + self.r > ground.y:
            self.vy = -abs(self.vy) / 2
            self.vx = self.vx * 0.8
            self.y -= 10

    def text(self):
        font = pygame.font.SysFont('arial', 32, True)
        text_1 = font.render("You hit the target with {} tries.".format(self.tries), True, BLACK)
        screen.blit(text_1, text_1.get_rect(center=(screen_x // 2, screen_y // 2)))


class Target:
    def __init__(self):
        self.color = RED
        self.r = ran(35, 45)
        self.x = ran(self.r, screen_x - self.r)
        self.y = ran(self.r, screen_y // 3 - self.r)
        self.v = self.r / 5
        self.angle = ran(0, int(2 * pi * 100))
        self.vx = self.v * cos(self.angle // 100)
        self.vy = self.v * sin(self.angle // 100)

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)
        circle(screen, WHITE, (self.x, self.y), 4 * self.r / 5)
        circle(screen, self.color, (self.x, self.y), 3 * self.r / 5)
        circle(screen, WHITE, (self.x, self.y), 2 * self.r / 5)
        circle(screen, self.color, (self.x, self.y), self.r / 5)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r > screen_x:
            self.vx = -abs(self.vx)
        if self.y + self.r > screen_y // 3:
            self.vy = -abs(self.vy)
        if self.x - self.r < 0:
            self.vx = abs(self.vx)
        if self.y - self.r < 0:
            self.vy = abs(self.vy)

    def is_touching(self, other: Bullet):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dist <= self.r + other.r


finished = False
clock = pygame.time.Clock()

score = 0
ground = Ground()
cannon = Cannon(40, y=ground.y)
target = [Target(), Target()]
bullet = []
while not finished:
    clock.tick(FPS)
    ground.draw()
    cannon.move()
    cannon.draw()
    score_count()
    for unit in bullet:
        unit.move()
        unit.draw()
    for one in target:
        one.draw()
        one.move()
        for bul in bullet:
            if one.is_touching(bul):
                screen.fill(WHITE)
                bul.tries = len(bullet)
                bul.text()
                pygame.display.update()
                pygame.time.wait(1000)
                bullet = []
                target = [Target(), Target()]
                score += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP:
            bullet.append(Bullet(cannon.x + cannon.side * cos(cannon.angle) + 0.5 * cannon.width * sin(cannon.angle),
                                 cannon.y + cannon.side * sin(cannon.angle) - 0.5 * cannon.width * cos(cannon.angle),
                                 1.3 * (cannon.side - cannon.start_side), cannon.width))

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
