from math import sin, cos, acos, pi
from random import randint as ran

import pygame
from pygame.draw import *

from my_colors import *

pygame.init()

FPS = 60
SCREEN_X, SCREEN_Y = 1200, 600
GROUND_Y = 19 * SCREEN_Y // 20

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.score = 0
        self.cannon = Cannon(40, y=GROUND_Y)
        self.targets = [Target(), Target()]
        self.bullets = []
        self.bombs = []
        self.butterflies = [Butterfly()]

    def score_count(self):
        font = pygame.font.SysFont('arial', 25, True)
        text_1 = font.render("Score: {}".format(self.score), True, BLACK)
        screen.blit(text_1, text_1.get_rect(center=(SCREEN_X // 25, SCREEN_Y // 50)))

    def ground_draw(self):
        line(screen, BLACK, (0, GROUND_Y), (SCREEN_X, GROUND_Y), 3)

    def add_butterfly(self):
        butterfly_number = self.score // 8 + 1
        if len(self.butterflies) < butterfly_number:
            self.butterflies.append(Butterfly())

    def mainloop(self):
        finished = False
        bullet_type_1 = True
        while not finished:
            self.clock.tick(FPS)
            self.ground_draw()
            self.cannon.move()
            self.cannon.muzzle_move()
            self.cannon.draw()
            self.cannon.health_draw()
            self.score_count()
            self.add_butterfly()

            if self.cannon.is_dead():
                finished = True

            for target in self.targets:
                target.move()
                target.draw()

            for bullet in self.bullets:
                if bullet.disappears(self.cannon):
                    self.bullets.remove(bullet)
                bullet.move()
                bullet.draw()

            for bomb in self.bombs:
                if bomb.disappears():
                    self.bombs.remove(bomb)
                bomb.move()
                bomb.draw()

            for butterfly in self.butterflies:
                butterfly.move()
                butterfly.draw()
                if butterfly.time_passed():
                    self.bombs.append(Bomb(butterfly, 10))
                    butterfly.waits()

            for bomb in self.bombs:
                if self.cannon.is_touching(bomb):
                    self.cannon.health -= self.cannon.max_health / 5
                    self.bombs.remove(bomb)

            for bullet in self.bullets:
                for target in self.targets:
                    if target.is_touching(bullet):
                        self.targets.remove(target)
                        self.targets.append(Target())
                        try:
                            self.bullets.remove(bullet)
                        except ValueError:
                            print("Congratulations you hit two butterflies with one shot!!!")
                        self.score += 1
                        if self.cannon.health_is_not_full():
                            self.cannon.health += self.cannon.max_health / 50

            for bullet in self.bullets:
                for butterfly in self.butterflies:
                    if butterfly.is_touching(bullet):
                        self.butterflies.remove(butterfly)
                        self.butterflies.append(Butterfly())
                        try:
                            self.bullets.remove(bullet)
                        except ValueError:
                            print("Congratulations you hit two butterflies with one shot!!!")
                        self.score += 1
                        if self.cannon.health_is_not_full():
                            self.cannon.health += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    bullet_type_1 = not bullet_type_1
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if bullet_type_1:
                        self.bullets.append(Bullet(self.cannon, self.cannon.width, self.cannon.angle))
                    else:
                        for delta_angle in range(-1, 2):
                            self.bullets.append(Bullet(self.cannon, self.cannon.width / 3,
                                                       self.cannon.angle + delta_angle / 35))

            pygame.display.update()
            screen.fill(WHITE)


class Timer:
    def __init__(self, lap=1000):
        self.lap = lap
        self.start_time = pygame.time.get_ticks()

    def time_passed(self):
        return pygame.time.get_ticks() > self.start_time + self.lap

    def waits(self):
        self.start_time = pygame.time.get_ticks()


class Cannon:
    def __init__(self, start_side, y, x=SCREEN_X / 2, color=ARMY, width=9):
        self.color = color
        self.start_side = start_side
        self.side = start_side
        self.r = start_side / 2
        self.x = x
        self.y = y - self.r - 2
        self.v = 10
        self.width = width
        self.side_v = start_side / 75
        self.angle = 0
        self.max_health = 50
        self.health = self.max_health

    def draw(self):
        circle(screen, ARMY, (self.x, self.y), self.r)
        rect(screen, ARMY, (self.x - 2 * self.r, self.y + self.width // 2 + 2, 4 * self.r, self.r - self.width // 2))
        polygon(screen, self.color, [(self.x - 0.5 * self.width * sin(self.angle),
                                      self.y + 0.5 * self.width * cos(self.angle)),
                                     (self.x - 0.5 * self.width * sin(self.angle) + self.side * cos(self.angle),
                                      self.y + 0.5 * self.width * cos(self.angle) + self.side * sin(self.angle)),
                                     (self.x + 0.5 * self.width * sin(self.angle) + self.side * cos(self.angle),
                                      self.y - 0.5 * self.width * cos(self.angle) + self.side * sin(self.angle)),
                                     (self.x + 0.5 * self.width * sin(self.angle),
                                      self.y - 0.5 * self.width * cos(self.angle))])

    def health_draw(self):
        rect(screen, RED, (150, 5, 1000, 20))
        if self.health > 0:
            rect(screen, GREEN, (150, 5, 1000 * self.health // self.max_health, 20))
        rect(screen, BLACK, (150, 5, 1000, 20), 3)

    def muzzle_move(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 0 > mouse_y - self.y:
            self.angle = -acos((mouse_x - self.x) / ((mouse_y - self.y) ** 2 + (mouse_x - self.x) ** 2) ** 0.5)

        if pygame.mouse.get_pressed(5)[0]:
            self.side += self.side_v
            if self.side > 1.7 * self.start_side:
                self.side_v = -abs(self.side_v)
            elif self.side < self.start_side:
                self.side_v = abs(self.side_v)

        else:
            self.side = self.start_side

    def move(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.x + 2 * self.r < SCREEN_X:
            self.x += self.v
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.x - 2 * self.r > 0:
            self.x -= self.v

    def is_touching(self, other):
        dist = ((self.x - other.x) ** 2 + (self.y + self.r - other.y) ** 2) ** 0.5
        return dist <= 2 * self.r + other.r

    def health_is_not_full(self):
        return self.health != self.max_health

    def is_dead(self):
        return self.health <= 0


class Ammunition:
    def __init__(self, color, x, y, r, vx, vy):
        self.color = color
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.g = 0.4

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.g

        if self.x + self.r > SCREEN_X:
            self.vx = -self.vx / 2
            self.vy = self.vy * 0.8
            self.x = SCREEN_X - self.r
        if self.x - self.r < 0:
            self.vx = -self.vx / 2
            self.vy = self.vy * 0.8
            self.x = self.r
        if self.y + self.r > GROUND_Y:
            self.vy = -self.vy / 2
            self.vx = self.vx * 0.8
            self.y = GROUND_Y - self.r


class Bullet(Ammunition):
    def __init__(self, other, r, angle):
        self.v = 1.3 * (other.side - other.start_side)
        super().__init__(GREY,
                         other.x + other.side * cos(other.angle),
                         other.y + other.side * sin(other.angle),
                         r,
                         self.v * cos(angle),
                         self.v * sin(angle))

    def disappears(self, other: Cannon):
        return self.vx ** 2 + self.vy ** 2 < other.start_side / 12 and self.y > GROUND_Y - 20 or \
               self.y < - 0.3 * SCREEN_Y


class Bomb(Ammunition):
    def __init__(self, other, r):
        super().__init__(BLACK, other.x, other.y, r, other.vx, other.vy)

    def disappears(self):
        return self.y >= GROUND_Y - self.r - self.vy


class Target:
    def __init__(self, bottom=GROUND_Y, top=0, left=0, right=SCREEN_X):
        self.color = RED
        self.r = ran(20, 25)
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom
        self.x = ran(self.left + self.r, self.right - self.r)
        self.y = ran(self.top + self.r, self.bottom - self.r)
        self.v = self.r / 4
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
        if self.x > self.right - self.r:
            self.vx = -abs(self.vx)
        if self.y > self.bottom - self.r:
            self.vy = -abs(self.vy)
        if self.x < self.left + self.r:
            self.vx = abs(self.vx)
        if self.y < self.top + self.r:
            self.vy = abs(self.vy)

    def is_touching(self, other: Bullet):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dist <= self.r + other.r


class Butterfly(Target, Timer):
    def __init__(self):
        Target.__init__(self)
        Timer.__init__(self)
        self.r = ran(25, 35)
        self.v = self.r / 2

    def draw(self):
        butterfly_pic = pygame.image.load('moonlight_butterfly.png')
        butterfly_pic = pygame.transform.scale(butterfly_pic, (self.r * 2, self.r * 2))
        screen.blit(butterfly_pic, (self.x - self.r, self.y - self.r))

    def is_touching(self, other: Bullet):
        dist_x = abs(self.x - other.x)
        dist_y = abs(self.y - other.y)
        return dist_x < self.r + other.r and dist_y < self.r + other.r


if __name__ == "__main__":
    try:
        game = Game()
        game.mainloop()
    finally:
        pygame.quit()
