import time
import turtle

turtle.shape('turtle')
turtle.speed(10000000000)

turtle.left(90)

step=3
angles = 75
for i in range (10):
    for i in range(angles):
        turtle.forward(step)
        turtle.left(360/angles)
    for i in range(angles):
        turtle.forward(step)
        turtle.right(360/angles)
    step +=0.5

turtle.hideturtle()
