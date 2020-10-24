import pygame
from pygame.draw import *
from random import randint as ran, choice
from math import pi, sin, cos, atan

pygame.init()
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
screen_x, screen_y = 800, 600
screen = pygame.display.set_mode((screen_x, screen_y))


class Cannon:
    def __init__(self, start_side, side, color=BLACK, cord_x=screen_x // 30, cord_y=9 * screen_y // 10, width=7):
        self.color = color
        self.start_side = start_side
        self.side = side
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.width = width

    def draw(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x - self.cord_x != 0:
            angle = atan((mouse_y - self.cord_y) / (mouse_x - self.cord_x))
            polygon(screen, self.color, [(self.cord_x, self.cord_y),
                                         (self.cord_x + self.side * cos(angle), self.cord_y + self.side * sin(angle))],
                    self.width)

    def move(self):
        if pygame.mouse.get_pressed()[0]:
            self.color = GREEN
            if self.side < 2 * self.start_side:
                self.side += 1
        else:
            self.side = self.start_side
            self.color = BLACK


class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        ellipse(screen, BLACK, (self.x, self.y, self.r, self.r))


finished = False
clock = pygame.time.Clock()
ball = Ball(ran(4 * screen_x // 5, screen_x), ran(0, screen_y), ran(30, 100))
cannon = Cannon(20, 20)
while not finished:
    clock.tick(FPS)
    ball.draw()
    cannon.move()
    cannon.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
