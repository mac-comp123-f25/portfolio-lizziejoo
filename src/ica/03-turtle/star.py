import turtle

window = turtle.Screen()
turtle_star = turtle.Turtle()
turtle_star.shape("circle")

for aColor in ["yellow", "yellow", "yellow", "yellow", "yellow"]:
    turtle_star.color(aColor)
    turtle_star.right(144)
    turtle_star.forward(100)

turtle_star.up()
turtle_star.goto(100, 100)
turtle_star.down()

for aColor in ["pink", "pink", "pink", "pink", "pink"]:
    turtle_star.color(aColor)
    turtle_star.right(144)
    turtle_star.forward(100)




window.exitonclick()
