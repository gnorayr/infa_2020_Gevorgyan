import turtle
import numpy as np
import time
turtle.shape('turtle')
turtle.speed(10000)

step0=20
turtle.left(150)
step=2*step0*np.sqrt(3)
angle = 3
for i in range(10):
    
    for k in range(angle):
        turtle.forward(step)
        turtle.left(360/angle)
    turtle.right(90+(180/angle))
    
    turtle.penup()
    turtle.forward(step0)
    turtle.pendown()

    angle += 1
    step = 2*(angle-1)*step0*np.sin(np.pi/angle)
    turtle.left(90+(180/angle))
    
    

turtle.hideturtle()
