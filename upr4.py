import turtle

turtle.shape('turtle')


fig1_angles = 360
for i in range(fig1_angles):
    turtle.forward(1)
    turtle.left(360/fig1_angles)

turtle.hideturtle()
