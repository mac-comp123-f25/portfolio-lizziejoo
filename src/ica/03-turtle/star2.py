import turtle

window = turtle.Screen()
turtle_star = turtle.Turtle()
turtle_star.shape("circle")
turtle_star.color("red")
turtle_star_pink = turtle.Turtle()
turtle_star_pink.color("blue")

for reps in range(5):
    turtle_star.right(144)
    turtle_star.forward(100)

turtle_star_pink.up()
turtle_star_pink.goto(100, 100)
turtle_star_pink.down()

for reps in range(5):
    turtle_star_pink.right(144)
    turtle_star_pink.forward(100)

window.exitonclick()
