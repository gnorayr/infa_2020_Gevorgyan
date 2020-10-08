import time
import turtle

turtle.shape('turtle')
turtle.speed(10000000000)

step=4
angles = 75
for i in range (3):
    for i in range(angles):
        turtle.forward(step)
        turtle.left(360/angles)
    for i in range(angles):
        turtle.forward(step)
        turtle.right(360/angles)
    turtle.left(60)

turtle.hideturtle()
