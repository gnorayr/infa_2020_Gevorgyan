import turtle
import math as m
import time

turtle.shape('turtle')
turtle.speed(7)

step=100
angle0=11
for i in range(angle0):
    turtle.forward(step)
    turtle.left(m.floor(angle0/2)*360/angle0)

turtle.penup()    
turtle.forward(step*2)    
turtle.pendown()

angle=5
for i in range(angle):
    turtle.forward(step)
    turtle.left(m.floor(angle/2)*360/angle)            
    
turtle.hideturtle()
