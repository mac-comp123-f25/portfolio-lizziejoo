import turtle

window = turtle.Screen()
my_turtle = turtle.Turtle()

for i in range(3):
    turtle.forward(100)
    turtle.right(120)

window.exitonclick()