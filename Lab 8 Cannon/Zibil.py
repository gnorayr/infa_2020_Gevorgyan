import pygame
from pygame.draw import *
from random import randint as ran, choice
from math import sin, cos, atan
from my_colors import *

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
    def __init__(self, start_side, color=BLACK, cord_x=screen_x // 30, cord_y=7 * screen_y // 10, width=7):
        self.color = color
        self.start_side = start_side
        self.side = start_side
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = width

    def draw(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x - self.cord_x != 0:
            angle = atan((mouse_y - self.cord_y) / (mouse_x - self.cord_x))
            polygon(screen, self.color, [(self.cord_x, self.cord_y),
                                         (self.cord_x + self.side * cos(angle), self.cord_y + self.side * sin(angle)),
                                         (self.cord_x + self.side * cos(angle) - self.width * sin(angle),
                                          self.cord_y + self.side * sin(angle) + self.width * cos(angle)),
                                         (self.cord_x - self.width * sin(angle),
                                          self.cord_y + self.width * cos(angle))])

    def move(self):
        if pygame.mouse.get_pressed()[0]:
            self.color = YELLOW
            if self.side < 4 * self.start_side:
                self.side += 0.8
        else:
            self.side = self.start_side
            self.color = BLACK


class Target:
    def __init__(self, x=ran(4 * screen_x // 5, screen_x - 50), y=ran(50, screen_y - 50), r=ran(10, 30)):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        ellipse(screen, RED, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))


class Bullet:
    def __init__(self, cord_x, cord_y, v, r=12, g=0.3):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angel = atan((cord_y - mouse_y) / (cord_x - mouse_x))
        self.color = choice(list(COLORS))
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.v = v
        self.vx = v * cos(self.angel)
        self.vy = v * sin(self.angel)
        self.r = r
        self.g = g
        self.tries = 0

    def move(self):
        if self.vx ** 2 + self.vy ** 2 > cannon.start_side / 12:
            ellipse(screen, self.color, (self.cord_x - self.r, self.cord_y - self.r, 2 * self.r, 2 * self.r))
            self.cord_x += self.vx
            self.cord_y += self.vy
            self.vy += self.g

    def ricochet(self):
        if self.cord_x + self.r > screen_x:
            self.vx = -abs(self.vx) / 2
            self.vy = self.vy * 0.8
            self.cord_x -= 10
        if self.cord_y + self.r > screen_y:
            self.vy = -abs(self.vy) / 2
            self.vx = self.vx * 0.8
            self.cord_y -= 10

    def text(self):
        font = pygame.font.SysFont('arial', 32, True)
        text_1 = font.render("You destroyed the target for {} shots.".format(self.tries), True, BLACK)
        screen.blit(text_1, text_1.get_rect(center=(screen_x // 2, screen_y // 2)))


finished = False
clock = pygame.time.Clock()

score = 0
cannon = Cannon(20)
target = [Target(ran(4 * screen_x // 5, screen_x - 50), ran(50, screen_y - 50), ran(10, 30))]
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
            if (bul.cord_x - one.x) ** 2 + (bul.cord_y - one.y) ** 2 <= (bul.r + one.r) ** 2:
                screen.fill(WHITE)
                bul.tries = len(bullet)
                bul.text()
                pygame.display.update()
                pygame.time.wait(3000)
                bullet = []
                target = target[:-1]
                target.append(Target(ran(4 * screen_x // 5, screen_x - 50), ran(50, screen_y - 50), ran(10, 30)))
                score += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP:
            bullet.append(Bullet(cannon.cord_x, cannon.cord_y, 0.7 * (cannon.side - cannon.start_side)))

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
