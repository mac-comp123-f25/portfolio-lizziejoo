import turtle


# ---- Functions ----

def draw_hook(t, size):
    """Draw a simple white string above the ornament."""
    t.pensize(2)
    t.pencolor("white")

    # Move to top of ornament
    t.penup()
    t.goto(0, size)
    t.setheading(90)
    t.pendown()

    # Draw string above ornament
    t.forward(size / 2)

    # Draw left loop
    t.right(45)
    t.circle(size / 6, 180)

    # Move back to center
    t.penup()
    t.goto(0, size + size / 2)
    t.setheading(135)
    t.pendown()

    # Draw right loop
    t.circle(-size / 6, 180)


def draw_ornament(t, color, size):
    """Draw the main ornament circle."""
    t.penup()
    t.goto(0, -size / 2)
    t.pendown()
    t.pensize(3)
    t.color("black", color)
    t.begin_fill()
    t.circle(size / 2)
    t.end_fill()


def draw_star(t, size):
    """Draw a small star inside the ornament."""
    t.penup()
    t.goto(0, -size / 6)
    t.pendown()
    t.color("white")
    for i in range(5):
        t.forward(size / 3)
        t.right(144)


def draw_snowflake(t, size):
    """Draw a simple snowflake pattern inside the ornament."""
    t.pensize(2)
    t.color("white")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for _ in range(6):
        t.forward(size / 3)
        t.backward(size / 3)
        t.right(60)
    # Add little branches on ends
    for _ in range(6):
        t.forward(size / 3)
        for angle in [45, -90, 45]:
            t.right(angle)
            t.forward(size / 10)
            t.backward(size / 10)
        t.backward(size / 3)
        t.right(60)


def draw_heart(t, size):
    """Draw a heart inside the ornament."""
    t.penup()
    t.goto(0, -size / 8)
    t.setheading(140)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.forward(size / 4)
    for i in range(200):
        t.right(1)
        t.forward(size / 800)
    t.left(120)
    for i in range(200):
        t.right(1)
        t.forward(size / 800)
    t.forward(size / 4)
    t.end_fill()


def main():
    screen = turtle.Screen()
    screen.title("Custom Ornament Designer")
    screen.bgcolor("lightblue")  #  light blue background

    t = turtle.Turtle()
    t.speed(8)

    # Ask user for customization
    ornament_color = screen.textinput("Ornament Color", "Enter a color for your ornament:")
    ornament_size = screen.numinput("Ornament Size", "Enter size (e.g., 100):", 100, 50, 200)
    shape_choice = screen.textinput("Shape", "Choose a shape: star, heart, or snowflake").lower()

    # Draw ornament
    draw_ornament(t, ornament_color, ornament_size)

    # Draw selected center shape
    if shape_choice == "star":
        draw_star(t, ornament_size)
    elif shape_choice == "heart":
        draw_heart(t, ornament_size)
    elif shape_choice == "snowflake":
        draw_snowflake(t, ornament_size)

    # Draw bow on top
    draw_hook(t, ornament_size / 2)

    # Hide turtle
    t.hideturtle()
    turtle.done()


# ---- Run the program ----
if __name__ == "__main__":
    main()



