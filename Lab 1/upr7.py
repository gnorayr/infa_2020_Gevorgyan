import turtle
import time

turtle.speed(1000)
turtle.shape('turtle')

step=0.1
angle = 360*10
for i in range(angle):
    turtle.forward(step)
    turtle.left(1)
    step +=0.001
    

turtle.hideturtle()
