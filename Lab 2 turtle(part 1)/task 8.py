import time
import turtle

turtle.shape('turtle')
turtle.speed(5)

rotations_number = 10
step = 20
length = step
for i in range(2*rotations_number):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    length += step

turtle.hideturtle()
