from random import randint
import turtle as t

t.up()
t.goto(-200 , 200)
t.down()
for i in range(4):
    t.fd(400)
    t.rt(90)
t.hideturtle()    

x_max , y_max = 200 , 200
number = 10
steps = 1000



pool = [t.Turtle(shape='circle' )   for i in range(number)]
for unit in pool:
    unit.shapesize(0.5)
    unit.penup()
    unit.speed(50)
    x = randint(-200, 200)
    y = randint(-200, 200)
    a = randint(0 , 360)
    unit.goto(x , y)
    unit.left(a)
    



for i in range(steps):
    
    for unit in pool:
        unit.fd(5)
        x = unit.xcor()
        y = unit.ycor()
        a = unit.heading()
        if  x_max - x < 0 or x_max + x < 0:
            unit.setheading(180 - a)
        
        if y_max - y < 0 or y_max + y < 0 :
            unit.setheading(-a)
            
