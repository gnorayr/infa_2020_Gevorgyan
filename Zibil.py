import pygame
from pygame.draw import *
from random import randint as ran, choice
from math import pi, sin, cos, atan

pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
screen_x, screen_y = 800, 600
screen = pygame.display.set_mode((screen_x, screen_y))


def canon(color, side, cord_x=screen_x // 30, cord_y=9 * screen_y // 10, width=7):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x - cord_x != 0:
        angle = atan((mouse_y - cord_y) / (mouse_x - cord_x))
        polygon(screen, color, [(cord_x, cord_y),
                                (cord_x + side * cos(angle), cord_y + side * sin(angle))], width)


class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        ellipse(screen, BLACK, (self.x, self.y, self.r, self.r))


a = 20
FPS = 60
finished = False
clock = pygame.time.Clock()
ball = Ball(ran(4 * screen_x // 5, screen_x), ran(0, screen_y), ran(30, 100))
while not finished:
    clock.tick(FPS)
    ball.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    key = pygame.mouse.get_pressed()[0]
    if key:
        canon(GREEN, side=a)
        if a < 50:
            a += 1
    else:
        a = 20
        canon(BLACK, side=a)
    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
