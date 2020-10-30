import pygame
from pygame.draw import *
from random import randint as ran, choice
from math import sin, cos, atan
from my_color import *

"Version pygame 2.0.0"
pygame.init()
FPS = 60
screen_x, screen_y = 800, 600
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


class Cannon:
    def __init__(self, start_side, color=ARMY, cord_x=screen_x // 25, cord_y=9 * screen_y // 10, width=9):
        self.color = color
        self.start_side = start_side
        self.side = start_side
        self.x = cord_x
        self.y = cord_y
        self.width = width
        self.side_v = start_side / 75
        self.r = start_side / 2

    def draw(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        circle(screen, ARMY, (self.x, self.y), self.r)
        rect(screen, ARMY, (self.x - 2 * self.r, self.y, 4 * self.r, self.r))
        rect(screen, BLACK, (0, 9 * screen_y / 10 + self.r, screen_x, 3))
        if mouse_x - self.x != 0:
            angle = atan((mouse_y - self.y) / (mouse_x - self.x))
            polygon(screen, self.color, [(self.x, self.y),
                                         (self.x + self.side * cos(angle), self.y + self.side * sin(angle)),
                                         (self.x + self.side * cos(angle) - self.width * sin(angle),
                                          self.y + self.side * sin(angle) + self.width * cos(angle)),
                                         (self.x - self.width * sin(angle),
                                          self.y + self.width * cos(angle))])

    def move(self):
        if pygame.mouse.get_pressed(3)[0]:
            self.side += self.side_v
            if self.side > 1.5 * self.start_side:
                self.side_v = -abs(self.side_v)
            elif self.side < 1.5 * self.start_side and self.side_v > 0:
                self.side_v = abs(self.side_v)
            elif self.side < self.start_side:
                self.side_v = abs(self.side_v)
            elif self.side < 1.5 * self.start_side and self.side_v < 0:
                self.side_v = -abs(self.side_v)

        else:
            self.side = self.start_side


class Target:
    def __init__(self, x, y, r):
        self.color = choice(list(COLORS))
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        ellipse(screen, self.color, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))


class Bullet:
    def __init__(self, cord_x, cord_y, v, r, g=0.3):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angel = atan((cord_y - mouse_y) / (cord_x - mouse_x))
        self.color = BLACK
        self.x = cord_x
        self.y = cord_y
        self.v = v
        self.vx = v * cos(self.angel)
        self.vy = v * sin(self.angel)
        self.r = r
        self.g = g
        self.tries = 0

    def move(self):
        if self.vx ** 2 + self.vy ** 2 > cannon.start_side / 12:
            ellipse(screen, self.color, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))
            self.x += self.vx
            self.y += self.vy
            self.vy += self.g

    def ricochet(self):
        if self.x + self.r > screen_x:
            self.vx = -abs(self.vx) / 2
            self.vy = self.vy * 0.8
            self.x -= 10
        if self.y + self.r > 9 * screen_y / 10 + cannon.r:
            self.vy = -abs(self.vy) / 2
            self.vx = self.vx * 0.8
            self.y -= 10

    def text(self):
        font = pygame.font.SysFont('arial', 32, True)
        text_1 = font.render("You destroyed the target with {} shots.".format(self.tries), True, BLACK)
        screen.blit(text_1, text_1.get_rect(center=(screen_x // 2, screen_y // 2)))


finished = False
clock = pygame.time.Clock()

score = 0
cannon = Cannon(40)
target = [Target(ran(4 * screen_x // 5, screen_x - 50), ran(2 * cannon.r, screen_y - 2 * cannon.r), ran(10, 30))]
bullet = []
while not finished:
    clock.tick(FPS)
    cannon.move()
    cannon.draw()
    score_count()
    for unit in bullet:
        unit.move()
        unit.ricochet()
    for one in target:
        one.draw()
        for bul in bullet:
            if (bul.x - one.x) ** 2 + (bul.y - one.y) ** 2 <= (bul.r + one.r) ** 2:
                screen.fill(WHITE)
                bul.tries = len(bullet)
                bul.text()
                pygame.display.update()
                pygame.time.wait(1000)
                bullet = []
                target = target[:-1]
                target.append(
                    Target(ran(4 * screen_x // 5, screen_x - 50), ran(2 * cannon.r, screen_y - 2 * cannon.r),
                           ran(10, 30)))
                score += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP:
            bullet.append(Bullet(cannon.x, cannon.y, 1.2 * (cannon.side - cannon.start_side), cannon.width))

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
