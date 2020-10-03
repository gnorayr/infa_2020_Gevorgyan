import turtle

turtle.shape('turtle')

fig1_angles = 12
for i in range(fig1_angles):
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180)
    turtle.left(360/fig1_angles)
    

turtle.hideturtle()
