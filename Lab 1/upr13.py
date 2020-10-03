import turtle
import time

turtle.shape('turtle')
turtle.speed(100000)

step=4
angle=200
turtle.begin_fill()
turtle.color('yellow')
for i in range(angle):
    turtle.forward(step)
    turtle.left(360/angle)
turtle.end_fill()

turtle.goto(60,170)
turtle.begin_fill()
turtle.color('blue')

for i in range(angle):
    turtle.forward(step/9)
    turtle.left(360/angle)
turtle.end_fill()

turtle.color('yellow')
turtle.goto(-60,170)
turtle.begin_fill()
turtle.color('blue')

for i in range(angle):
    turtle.forward(step/9)
    turtle.left(360/angle)
turtle.end_fill()

turtle.color('yellow')
turtle.goto(0,100)
turtle.color('black')
turtle.left(90)
turtle.width(10)
turtle.forward(45)

turtle.penup()
turtle.goto(-64,85)
turtle.pendown()
turtle.color('red')

for i in range(100):
    turtle.backward(step/2)
    turtle.left(360/angle)




turtle.hideturtle()
