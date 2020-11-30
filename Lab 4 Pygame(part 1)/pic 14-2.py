import pygame
from pygame.draw import *
from math import pi


pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


def grass():
    rect(screen, (55, 200, 113), (0, 250, 600, 600))


def fense(x1 = 0, y1 = 100, x2 = 400, y2 = 350):
    N = 19
    line(screen, (0,0,0), (x1, y2), (x2, y2))
    rect(screen, (200, 171, 55), (x1, y1, x2 - x1, y2 - y1))
    h = (x2 - x1) / (N + 1)
    x = x1 + h
    for i in range(N):
        line(screen, (0,0,0), (x, y1), (x, y2))
        x += h

def sky():
    rect(screen, (95, 188, 211), (0, 0, 600, 300))
    
    

def dog(n = 1, x = 50, y = 400):
    color=(108, 103, 83)
    def body() :
        chest = ellipse(screen, color, (x+75*n-55*abs(n), y+25*abs(n), 110*abs(n), 60*abs(n)))
        back = ellipse(screen, color, (x+115*n-35*abs(n), y+18*abs(n), 70*abs(n), 40*abs(n)))
        leg_1 = ellipse(screen, color, (x+65*n-15*abs(n), y+45*abs(n), 30*abs(n), 70*abs(n)))
        leg_2 = ellipse(screen, color, (x+25*n-15*abs(n), y+35*abs(n), 30*abs(n), 70*abs(n)))
        foot_1 = ellipse(screen, color, (x+55*n-15*abs(n), y+110*abs(n), 30*abs(n), 15*abs(n)))
        foot_2 = ellipse(screen, color, (x+15*n-15*abs(n), y+100*abs(n), 30*abs(n), 15*abs(n)))
        thigh_1 = circle(screen, color, (x+int(100*n), y+int(35*abs(n))), int(20*abs(n)))
        thigh_2 = circle(screen, color, (x+int(145*n), y+int(60*abs(n))), int(20*abs(n)))
        leg_3 = ellipse(screen, color, (x+118*n-8*abs(n), y+45*abs(n), 16*abs(n), 50*abs(n)))
        leg_4 = ellipse(screen, color, (x+158*n-8*abs(n), y+70*abs(n), 16*abs(n), 40*abs(n)))
        foot_3 = ellipse(screen, color, (x+110*n-10*abs(n), y+90*abs(n), 20*abs(n), 10*abs(n)))
        foot_4 = ellipse(screen, color, (x+150*n-10*abs(n), y+105*abs(n), 20*abs(n), 10*abs(n)))
    body()
    def head():
        dark = (40, 39, 31)
        s = 56
        eye_x = s/4
        eye_y = s/8
        ear_x = s/5
        ear_y = s/3
        head= rect(screen, color, (x+s/2*n-s/2*abs(n), y, s*abs(n), s*abs(n)))
        head= rect(screen, dark, (x+s/2*n-s/2*abs(n), y, s*abs(n), s*abs(n)), 2)
        #ear1
        ellipse(screen, color, (x-ear_x/2*abs(n), y, ear_x*abs(n), ear_y*abs(n)))
        ellipse(screen, dark, (x-ear_x/2*abs(n), y, ear_x*abs(n), ear_y*abs(n)), 2)
        #ear2
        ellipse(screen, color, (x+s*n-ear_x/2*abs(n), y, ear_x*abs(n), ear_y*abs(n)))
        ellipse(screen, dark, (x+s*n-ear_x/2*abs(n), y, ear_x*abs(n), ear_y*abs(n)), 2)
        #eye1
        ellipse(screen, (255, 255, 255), (x+(s/8+eye_x/2)*n-eye_x/2*abs(n), y + s/4*abs(n), eye_x*abs(n), eye_y*abs(n)))
        ellipse(screen, dark, (x+(s/8+eye_x/2)*n-eye_x/2*abs(n), y + s/4*abs(n), eye_x*abs(n), eye_y*abs(n)), 1)
        circle(screen, (0,0,0), (x+int(s/4*n), y+int(5*s/16*abs(n))), int(s/16*abs(n)))
        #eye2
        ellipse(screen, (255, 255, 255), (x+(5*s/8+eye_x/2)*n-eye_x/2*abs(n), y + s/4*abs(n), eye_x*abs(n), eye_y*abs(n)))
        ellipse(screen, dark, (x+(5*s/8+eye_x/2)*n-eye_x/2*abs(n), y + s/4*abs(n), eye_x*abs(n), eye_y*abs(n)), 1)
        circle(screen, (0,0,0), (x+int(3*s/4*n), y+int(5*s/16*abs(n))), int(s/16*abs(n)))
        #mouth
        angle = pi/16
        end_angle = pi
        l=s/3
        arc(screen, (0, 0, 0), (x+(s/4+0.75*l)*n-0.75*l*abs(n), y+3*s/4*abs(n), 1.5*l*abs(n), l*abs(n)), angle, end_angle)
        # teeth
        polygon(screen, (255, 255, 255), [(x+s/3*n, y+4*s/5*abs(n)), (x+s/3*n,y+7*s/10*abs(n)),
                                          (x+7*s/18*n, y+15*s/20*abs(n))])
        polygon(screen, (255, 255, 255), [(x+(s-s/3)*n, y+4*s/5*abs(n)), (x+(s-s/3)*n, y+7*s/10*abs(n)),
                                          (x+(s-7*s/18)*n, y+15*s/20*abs(n))])
    head()

def dog_house():
    x, y = 275, 375
    def walls():
        polygon(screen, (200, 171, 55), [(x, y), (x+75, y+30), (x+100, y),
                                         (x+100, y+80), (x+75, y+110), (x, y+80)])
        polygon(screen, (0,0,0), [(x, y), (x+75, y+30), 
                                  (x+75, y+110), (x, y+80)], 1)
        polygon(screen, (0,0,0), [(x+75, y+30), (x+100, y),
                                  (x+100, y+80), (x+75, y+110)], 1)
        ellipse(screen, (0,0,0),(x+17, y+32, 40, 45))
    walls()
    def roof():
        polygon(screen, (212, 170, 0), [(x, y), (x+75, y+30),
                                        (x+100, y), (x+70, y-70), (x+40, y-55)])
        polygon(screen, (0,0,0), [(x, y), (x+75, y+30),
                                  (x+40, y-55)], 1)
        polygon(screen, (0,0,0), [(x+75, y+30), (x+100, y),
                                  (x+70, y-70), (x+40, y-55)], 1)
    roof()
    def chain():
        ellipse(screen, (0,0,0), (x+10, y+70, 25, 10), 1)
        ellipse(screen, (0,0,0), (x+5, y+70, 15, 20), 1)
        ellipse(screen, (0,0,0), (x-5, y+80, 20, 15), 1)
        ellipse(screen, (0,0,0), (x-15, y+90, 25, 10), 1)
        ellipse(screen, (0,0,0), (x-20, y+93, 15, 15), 1)
        ellipse(screen, (0,0,0), (x-35, y+101, 25, 10), 1)
        ellipse(screen, (0,0,0), (x-45, y+105, 20, 10), 1)
        ellipse(screen, (0,0,0), (x-55, y+105, 15, 8), 1)
    
    chain()
    
        
    
sky()
grass()
fense(75, 25, 700, 300)
fense(-50, 100, 225, 300)
fense(185, 150, 500, 325)
fense(-50, 200, 175, 350)
dog(-0.75, 400, 300)
dog(-0.9, 200, 450)
dog(1, 50, 300)
dog_house()
dog(2, 300, 450)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
