import turtle

turtle1 = turtle.Turtle()
turtle1.color('yellow')
turtle1.pensize(50)
turtle1.shape('circle')

turtle1.begin_fill()
for x in range(5):
    turtle1.right(144)
    turtle1.forward(300)
turtle1.end_fill()

