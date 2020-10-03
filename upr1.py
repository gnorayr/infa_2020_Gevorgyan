import time
import turtle


def main():
    init()
    spiral()
    turtle.forward(100)
    spiral(5, 5)
    turtle.forward(100)
    spiral(step=5)
    turtle.hideturtle()


def init():
    turtle.shape('turtle')
    time.sleep(2)  # тех.момент. Вам не надо
    turtle.speed(10)
    turtle.color('green', 'yellow')
    turtle.penup()


def spiral(rotations_number=3, step=10):
    turtle.pendown()
    length = step
    for i in range(2*rotations_number):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        length += step
    turtle.penup()


main()
