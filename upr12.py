import turtle
import time

turtle.shape('turtle')
turtle.speed(10000000)

turtle.left(90)

step=1.5
angle=75
for i in range(5):
    for j in range(angle):
        turtle.forward(step)
        turtle.right(180/angle)
    if i==4:
        break
    for j in range(angle):
        turtle.forward(step/5)
        turtle.right(180/angle)



turtle.hideturtle()
