import turtle
import math

def drawFiveCircles(turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
    """This function draws five circles on the screen given a 
    turtle, radius, and coordinates."""

""" Drawing boundaries of petal and filling it green. 
Petals are drawn counterclockwise on top of each other, 
being drawn from the center.
4 turtles in the code. """

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFiveCircles(sepalTurtle, 50, 0, 0)

drawFiveCircles(petalTurtle, 25, 0, 0)

centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 0, 220)

drawFiveCircles(petalTurtle, 25, 0, 220)

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 220, 0)

drawFiveCircles(petalTurtle, 25, 220, 0)

centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 0, -220)

drawFiveCircles(petalTurtle, 25, 0, -220)

centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, -220, 0)

drawFiveCircles(petalTurtle, 25, -220, 0)

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()