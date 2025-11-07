import turtle

def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_hood(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.right(45)
    t.forward(size / 2)
    t.right(45)
    t.forward(size)
    t.right(45)
    t.forward(size / 2)
    t.right(135)
    t.forward(size * 1.5)
    t.end_fill()

def draw_hoodie(size, base_color, pattern):
    screen = turtle.Screen()
    screen.title("Custom Hoodie Design")
    t = turtle.Turtle()
    t.speed(5)
    t.pensize(2)

    t.up()
    t.goto(-size / 2, size / 2)
    t.down()
    draw_rectangle(t, size, size * 1.2, base_color)

    # Add sleeves, hood, and optional pattern here...

    t.hideturtle()
    turtle.done()  # Keeps the window open

size = int(input("Enter hoodie size (100-300): "))
base_color = input("Enter hoodie base color (e.g., blue, red, green): ")
pattern = input("Enter pattern type (stripes, polka dots, or plain): ")

if size < 100 or size > 300:
    print("Size out of range, using default size 200.")
    size = 200

draw_hoodie(size, base_color, pattern)
