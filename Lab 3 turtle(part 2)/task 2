import turtle as t
import time

t.shape('turtle')
t.color('blue')



s = 20
L = s * (2**(0.5))
b = 45
t.penup()
t.goto(-6*s , 0)
t.pendown()

def draw(route):
    for  angle, step, pen in route:
        if pen == 0 :
            t.penup()
        else :
            t.pendown()
        
        t.rt(angle)
        t.fd(step)
        
m = [
    
    [(0, s, 1) , (2*b , 2*s , 1 ) , (2*b , s , 1) , (2*b , 2*s , 1 ) , (2*b , 2*s , 0 )] ,
    [(2*b , s , 0) , (-3*b , L , 1) , (3*b , 2*s , 1) , (4*b , 2*s , 0) , (2*b , s , 0)] ,
    [(0 , s , 1) , (2*b , s , 1) , (b , L , 1) , (-3*b , s , 1) , (-2*b , 2*s , 0) , (2*b , s , 0)] ,
    [(0 , s , 1) , (3*b , L , 1) , (-3*b , s , 1) , (3*b , L , 1) , (3*b , 2*s , 0) , (2*b , 2*s , 0)] ,
    [(2*b , s , 1) , (-2*b , s , 1) , (2*b , s , 1) , (4*b , 2*s , 1) , (2*b , s , 0)] ,
    [(2*b , 2*s , 0) , (-2*b , s , 1) , (-2*b , s , 1) , (-2*b , s , 1) , (2*b , s , 1) , (2*b , s , 1) , (0 , s , 0)] ,
    [(0 , s , 0) , (3*b , L , 1) , (-b , s , 1) , (-2*b , s , 1) , (-2*b , s , 1) , (-2*b , s , 1) , (2*b , s , 0) , (2*b , 2*s , 0)] , 
    [(0 , s , 1) , (3*b , L , 1) , (-b , s , 1) , (4*b , 2*s , 0) , (2*b , 2*s , 0)] ,
    [(0, s, 1) , (2*b , 2*s , 1 ) , (2*b , s , 1) , (2*b , s , 1 ) , (2*b , s , 1) , (4*b , s , 1) , (2*b , s , 1) , (2*b , 2*s , 0 )] ,
    [(0 , s , 1) , (2*b , s , 1) , (b , L , 1) , (4*b , L , 1) , (-3*b , s , 1) , (2*b , s , 1) , (2*b , 2*s , 0 )]

    ]

draw(m[1])
draw(m[4])
draw(m[1])
draw(m[7])
draw(m[0])
draw(m[0])


t.hideturtle()
