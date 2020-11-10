import pygame
from pygame.draw import *
from random import randint as ran
from math import sin, cos, acos, pi

from my_colors import *

"Version pygame 2.0.0"
pygame.init()
FPS = 60
screen_x, screen_y = 1200, 600
screen = pygame.display.set_mode((screen_x, screen_y))


def score_count():
    font = pygame.font.SysFont('arial', 25, True)
    text_1 = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(text_1, text_1.get_rect(center=(screen_x // 15, screen_y // 15)))


def tries_count():
    tries = len(bullet)
    font = pygame.font.SysFont('arial', 25, True)
    text_1 = font.render("Tries: {}".format(tries), True, BLACK)
    screen.blit(text_1, text_1.get_rect(center=(screen_x // 15, screen_y // 10)))


class Timer:
    def __init__(self, lap):
        self.lap = lap
        self.start_time = pygame.time.get_ticks()

    def time(self):
        return self.start_time + self.lap > pygame.time.get_ticks()


class Ground:
    def __init__(self, y=19 * screen_y // 20):
        self.y = y

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
        self.v = 1.1
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

    def muzzle_move(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 0 > mouse_y - self.y:
            self.angle = -acos((mouse_x - self.x) / ((mouse_y - self.y) ** 2 + (mouse_x - self.x) ** 2) ** 0.5)

        if pygame.mouse.get_pressed(3)[0]:
            self.side += self.side_v
            if self.side > 1.7 * self.start_side:
                self.side_v = -abs(self.side_v)
            elif self.side < self.start_side:
                self.side_v = abs(self.side_v)

        else:
            self.side = self.start_side

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.x += self.v
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.x -= self.v


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


class Target:
    def __init__(self, bottom=screen_y, top=0, left=0, right=screen_x):
        self.color = RED
        self.r = ran(20, 25)
        self.right = right - self.r
        self.left = left + self.r
        self.top = top + self.r
        self.bottom = bottom - self.r
        self.x = ran(self.left, self.right)
        self.y = ran(self.top, self.bottom)
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
        if self.x > self.right:
            self.vx = -abs(self.vx)
        if self.y > self.bottom:
            self.vy = -abs(self.vy)
        if self.x < self.left:
            self.vx = abs(self.vx)
        if self.y < self.top:
            self.vy = abs(self.vy)

    def is_touching(self, other: Bullet):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dist <= self.r + other.r


finished = False
clock = pygame.time.Clock()

score = 0
ground = Ground()
cannon = Cannon(40, y=ground.y)
target_list = [Target(ground.y) for i in range(2)]
bullet = []
while not finished:
    clock.tick(FPS)
    ground.draw()
    cannon.move()
    cannon.draw()
    cannon.muzzle_move()
    score_count()
    tries_count()
    for unit in bullet:
        unit.move()
        unit.draw()
    for target in target_list:
        target.draw()
        target.move()
        for bul in bullet:
            if target.is_touching(bul):
                target_list.remove(target)
                target_list.append(Target(ground.y))
                bullet = []
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
