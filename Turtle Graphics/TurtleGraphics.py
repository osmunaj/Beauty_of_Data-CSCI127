import turtle

wn = turtle.Screen()
#alex = turtle.Turtle()

#for i in range(365):
#    alex.forward(1)
#    alex.left(1)
#    alex.speed(i)
#    alex.circle(i)


logo = turtle.Turtle()
logo.color("black", "red")
for i in range(4):
    logo.forward(100)
    logo.left(90)
logo.penup()
logo.forward(10)
logo.left(90)
logo.forward(10)

logo.right(90)
logo.pendown()
logo.begin_fill()
logo.pencolor("red")
for i in range(4):
    logo.forward(80)
    logo.left(90)
logo.end_fill()
