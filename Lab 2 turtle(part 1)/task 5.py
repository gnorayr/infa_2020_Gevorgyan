import turtle

    
number=10
step=20
length = step

for i in range(number):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.penup()
        turtle.forward(step/2)
        turtle.right(90)
        turtle.forward(step/2)
        turtle.right(180)
        turtle.pendown()
        length += step


turtle.hideturtle()
