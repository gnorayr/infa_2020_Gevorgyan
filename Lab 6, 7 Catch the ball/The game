import pygame
from pygame.draw import *
from random import randint
from math import pi, sin, cos
import csv
from time import asctime

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width, screen_height = 1200, 600


def main():
    global rects, balls, user_name
    """
    Initializes pygame Surface, defines event handling loop.
    """
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))

    FPS = 50
    score = 0
    user_name = ""
    lap = 3.5

    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        balls = parameters(number=3, size=55, v=3)
        rects = parameters(number=2, size=25, v=4)
        start_time = time(pygame.time.get_ticks(), 0, lap)
        present_time = 0
        while (present_time - start_time) / 1000 < lap:
            present_time = pygame.time.get_ticks()
            rects_move(screen)
            balls_move(screen)
            ricochet(balls)
            ricochet(rects)
            show_score(screen, score)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    while not finished:
                        dialog(screen, score)
                        finished = user_text(screen, score)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    score = click(score)
            pygame.display.update()
            screen.fill(BLACK)

    pygame.quit()


def parameters(number, size, v=3):
    """
    sets item parameters of items and puts in list
    :param number: number of items
    :param size: characteristic size of the items
    :param v: velocity
    :return: list with items
    """
    param = []
    for i in range(number):
        angle = randint(0, int(2 * pi * 100))
        param.append({
            'x': randint(100, screen_width - 100),
            'y': randint(100, screen_height - 100),
            'vx': v * cos(angle / 100),
            'vy': v * sin(angle / 100),
            'r': randint(40, 255),
            'g': randint(40, 255),
            'b': randint(40, 255),
            's': size
        })
    return param


def balls_move(surface):
    """
    moves the balls to the new place
    :param surface: pygame Surface object
    :return: none
    """
    for item in balls:
        ellipse(surface, (item['r'], item['g'], item['b']),
                (item['x'] - item['s'], item['y'] - item['s'], 2 * item['s'], 2 * item['s']))
        item['x'] += item['vx']
        item['y'] += item['vy']


def rects_move(surface):
    """
    moves the rectangles to the new place
    :param surface: pygame Surface object
    :return: none
    """
    for item in rects:
        rect(surface, (item['r'], item['g'], item['b']),
             (item['x'] - item['s'], item['y'] - item['s'], 2 * item['s'], 2 * item['s']))
        item['x'] += item['vx']
        item['y'] += item['vy']


def ricochet(param):
    """
    changes the velocity of items after hitting the walls
    :param param: list of items' parameters
    :return: none
    """
    for item in param:
        if item['x'] - item['s'] <= 0:
            item['vx'] = abs(item['vx'])
        if item['y'] - item['s'] <= 0:
            item['vy'] = abs(item['vy'])
        if item['x'] + item['s'] >= screen_width:
            item['vx'] = -abs(item['vx'])
        if item['y'] + item['s'] >= screen_height:
            item['vy'] = -abs(item['vy'])


def show_score(surface, score):
    """
    shows player's score in top left corner of the screen
    :param surface: pygame Surface object
    :param score: player's score
    :return: none
    """
    font = pygame.font.SysFont('arial', 25, True)
    text_1 = font.render("Score : {}".format(score), True, WHITE)
    surface.blit(text_1, (0, 0))


def dialog(surface, score):
    """
    At the end of the game shows text with score and
    asks player their name
    :param surface: pygame Surface object
    :param score: player's score
    :return: none
    """
    surface.fill(BLACK)
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render("Your score is {}".format(score), True, WHITE)
    text_2 = font.render("Please enter your name and press F1(or q to quit)", True, WHITE)
    surface.blit(text_1, text_1.get_rect(center=(screen_width / 2, screen_height / 3)))
    surface.blit(text_2, text_2.get_rect(center=(screen_width / 2, screen_height * 2 / 3)))


def user_text(surface, score):
    """
    takes the text typed on the screen and writes the achievement in a csv file
    :param surface: pygame Surface object
    :param score: player's score
    :return: True if pressed 'q', 'esc' or 'F1'
    """
    global user_name
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render(user_name, True, WHITE)
    surface.blit(text_1, text_1.get_rect(center=(screen_width / 2, screen_height / 2)))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_BACKSPACE:
                user_name = user_name[:-1]
            elif events.key == pygame.K_ESCAPE or events.key == pygame.K_q:
                return True
            elif events.key == pygame.K_F1:
                if user_name != "":
                    with open('Best scores.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([user_name, score, asctime()])
                return True
            else:
                user_name += events.unicode


def click(score):
    """
    checks if click was in the item. If yes returns the score.
    :param score: player's score
    :return: score
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for item in balls:
        if (mouse_x - item['x']) ** 2 + (mouse_y - item['y']) ** 2 <= item['s'] ** 2:
            score += 1
            item['x'], item['y'] = 2 * screen_width, 2 * screen_height
            item['vx'], item['vy'] = 0, 0
    for item in rects:
        if -item['s'] <= mouse_x - item['x'] <= item['s'] and -item['s'] <= mouse_y - item['y'] <= item['s']:
            score += 3
            item['x'], item['y'] = 2 * screen_width, 2 * screen_height
            item['vx'], item['vy'] = 0, 0
    return score


def time(present_t, start_t, lap):
    """
    calculates the starting time of the present lap
    :param present_t: present time
    :param start_t: starting time of the lap
    :param lap: duration of the lap
    :return: starting time of the present lap
    """
    if present_t - start_t >= lap:
        start_t = present_t
    return start_t


if __name__ == '__main__':
    main()
