import turtle

window = turtle.Screen()
turt = turtle.Turtle()
turt.shape("turtle")
turt.color("black")

turt.begin_fill()
for reps in range(2):
    turt.forward(100)
    turt.left(125)
turt.end_fill()

window.exitonclick()
