import pygame
from pygame.draw import *
from math import pi

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def grass():
    rect(screen, (55, 200, 113), (0, 350, 600, 250))


def fence():
    x1 = 0
    y1 = 100
    x2 = 500
    y2 = 350
    line(screen, (0, 0, 0), (0, y2), (x2, y2))
    N = 19
    color = (200, 171, 55)
    rect(screen, color, (x1, y1, x2 - x1, y2 - y1))
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N):
        line(screen, (0, 0, 0), (x, y1), (x, y2))
        x += h


def sky():
    rect(screen, (95, 188, 211), (0, 0, 600, 100))


def dog():
    color = (108, 103, 83)
    x, y = 50, 400

    def body():
        chest = ellipse(screen, color, (x + 20, y + 25, 110, 60))
        back = ellipse(screen, color, (x + 80, y + 18, 70, 40))
        leg_1 = ellipse(screen, color, (x + 50, y + 45, 30, 70))
        leg_2 = ellipse(screen, color, (x + 10, y + 35, 30, 70))
        foot_1 = ellipse(screen, color, (x + 40, y + 110, 30, 15))
        foot_2 = ellipse(screen, color, (x, y + 100, 30, 15))
        thigh_1 = circle(screen, color, (x + 100, y + 35), 20)
        thigh_2 = circle(screen, color, (x + 145, y + 60), 20)
        leg_3 = ellipse(screen, color, (x + 110, y + 45, 15, 50))
        leg_4 = ellipse(screen, color, (x + 150, y + 70, 15, 40))
        foot_3 = ellipse(screen, color, (x + 100, y + 90, 20, 10))
        foot_4 = ellipse(screen, color, (x + 140, y + 105, 20, 10))

    body()

    def head():
        dark = (40, 39, 31)
        s = 56
        eye_x = s / 4
        eye_y = s / 8
        ear_x = s / 5
        ear_y = s / 3
        head = rect(screen, color, (x, y, s, s))
        head = rect(screen, dark, (x, y, s, s), 2)
        # ear1
        ellipse(screen, color, (x - ear_x / 2, y, ear_x, ear_y))
        ellipse(screen, dark, (x - ear_x / 2, y, ear_x, ear_y), 2)
        # ear2
        ellipse(screen, color, (x + s - ear_x / 2, y, ear_x, ear_y))
        ellipse(screen, dark, (x + s - ear_x / 2, y, ear_x, ear_y), 2)
        # eye1
        ellipse(screen, (255, 255, 255), (x + s / 8, y + s / 4, eye_x, eye_y))
        ellipse(screen, dark, (x + s / 8, y + s / 4, eye_x, eye_y), 1)
        circle(screen, (0, 0, 0), (x + int(s / 4), y + int(5 * s / 16)), int(s / 16))
        # eye2
        ellipse(screen, (255, 255, 255), (x + 5 * s / 8, y + s / 4, eye_x, eye_y))
        ellipse(screen, dark, (x + 5 * s / 8, y + s / 4, eye_x, eye_y), 1)
        circle(screen, (0, 0, 0), (x + int(3 * s / 4), y + int(5 * s / 16)), int(s / 16))
        # mouth
        s = 56
        angle = pi / 16
        end_angle = pi
        l = s / 3
        arc(screen, (0, 0, 0), (x + s / 4, y + 3 * s / 4, 1.5 * l, l), angle, end_angle)
        # teeth
        polygon(screen, (255, 255, 255), [(x + s / 3, y + 4 * s / 5), (x + s / 3, y + 7 * s / 10),
                                          (x + 7 * s / 18, y + 15 * s / 20)])
        polygon(screen, (255, 255, 255), [(x + s - s / 3, y + 4 * s / 5), (x + s - s / 3, y + 7 * s / 10),
                                          (x + s - 7 * s / 18, y + 15 * s / 20)])

    head()


def dog_house():
    x, y = 275, 375

    def walls():
        polygon(screen, (200, 171, 55), [(x, y), (x + 75, y + 30), (x + 100, y),
                                         (x + 100, y + 80), (x + 75, y + 110), (x, y + 80)])
        polygon(screen, (0, 0, 0), [(x, y), (x + 75, y + 30),
                                    (x + 75, y + 110), (x, y + 80)], 1)
        polygon(screen, (0, 0, 0), [(x + 75, y + 30), (x + 100, y),
                                    (x + 100, y + 80), (x + 75, y + 110)], 1)
        ellipse(screen, (0, 0, 0), (x + 17, y + 32, 40, 45))

    walls()

    def roof():
        polygon(screen, (212, 170, 0), [(x, y), (x + 75, y + 30),
                                        (x + 100, y), (x + 70, y - 70), (x + 40, y - 55)])
        polygon(screen, (0, 0, 0), [(x, y), (x + 75, y + 30),
                                    (x + 40, y - 55)], 1)
        polygon(screen, (0, 0, 0), [(x + 75, y + 30), (x + 100, y),
                                    (x + 70, y - 70), (x + 40, y - 55)], 1)

    roof()

    def chain():
        ellipse(screen, (0, 0, 0), (x + 10, y + 70, 25, 10), 1)
        ellipse(screen, (0, 0, 0), (x + 5, y + 70, 15, 20), 1)
        ellipse(screen, (0, 0, 0), (x - 5, y + 80, 20, 15), 1)
        ellipse(screen, (0, 0, 0), (x - 15, y + 90, 25, 10), 1)
        ellipse(screen, (0, 0, 0), (x - 20, y + 93, 15, 15), 1)
        ellipse(screen, (0, 0, 0), (x - 35, y + 101, 25, 10), 1)
        ellipse(screen, (0, 0, 0), (x - 45, y + 105, 20, 10), 1)
        ellipse(screen, (0, 0, 0), (x - 55, y + 105, 15, 8), 1)

    chain()


grass()
fence()
sky()
dog()
dog_house()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
