import turtle
import random


# --- Helper Functions ---

def turtle_cleanup(t):
    """Lifts the pen, hides the turtle, and resets heading."""
    t.up()
    t.hideturtle()
    t.setheading(0)
    t.goto(0, 0)


def draw_rectangle(t, width, height, color):
    """Draw a filled rectangle."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def draw_hood(t, width, color, y_offset):
    """Draw the hood centered on top, incorporating a vertical offset."""

    t.up()
    # Move to the TOP-CENTER of the main hoodie body
    t.goto(0, width / 2 + y_offset)  # Use the corrected top Y-coordinate
    t.setheading(90)
    t.down()

    t.fillcolor(color)
    t.begin_fill()

    # 1. Move left to start the semi-circle (half the width of the hood's base)
    t.left(90)
    t.forward(width / 2)

    # 2. Draw the semi-circle
    t.right(90)
    t.circle(width / 2, 180)

    # 3. Close the shape by drawing back to the starting point (top-center)
    t.right(90)
    t.forward(width / 2)

    t.end_fill()
    turtle_cleanup(t)


def draw_stripes(t, size, height, y_offset):
    """Draw vertical pastel stripes over the main body area, incorporating offset."""
    t.width(1)
    stripe_width = size / 10
    start_y = size / 2 + y_offset  # Use corrected start Y

    stripe_colors = ["#FADADD", "#B0E0E6", "#E6E6FA"]

    for i in range(10):
        t.up()
        t.goto(-size / 2 + i * stripe_width, start_y)
        t.setheading(0)
        t.down()

        t.fillcolor(random.choice(stripe_colors))
        t.begin_fill()

        for _ in range(2):
            t.forward(stripe_width)
            t.right(90)
            t.forward(height)
            t.right(90)
        t.end_fill()
    turtle_cleanup(t)


def draw_polka_dots(t, size, height, y_offset):
    """Draw polka dots pattern within the main body, incorporating offset."""
    t.up()
    dot_colors = ["lightpink", "lightyellow", "lightgreen", "lightblue"]

    x_range = range(-int(size / 2) + 15, int(size / 2), 30)
    # Adjust Y range by the offset
    y_range = range(int(size / 2) - 15 + y_offset, int(size / 2) - int(height) + y_offset, -30)

    for x in x_range:
        for y in y_range:
            t.goto(x, y)
            t.dot(10, random.choice(dot_colors))
    turtle_cleanup(t)


def draw_gingham(t, size, height, y_offset):
    """Draw gingham (checkered) pattern over the main body, incorporating offset."""
    square_size = 20
    colors = ["#FADADD", "#E6E6FA"]

    num_x = int(size // square_size)
    num_y = int(height // square_size)

    for i in range(num_x):
        for j in range(num_y):
            t.up()
            # Adjust Y coordinate by the offset
            t.goto(-size / 2 + i * square_size, size / 2 - j * square_size + y_offset)
            t.setheading(0)
            t.down()

            t.fillcolor(colors[(i + j) % 2])
            t.begin_fill()

            for _ in range(4):
                t.forward(square_size)
                t.right(90)
            t.end_fill()
    turtle_cleanup(t)


# --- Main Drawing Function ---

def draw_hoodie(size, base_color, pattern):
    """Main function to draw the hoodie components with guaranteed centering."""
    screen = turtle.Screen()
    screen.title("Custom Hoodie Design")
    screen.setup(width=size + 150, height=size * 2)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    width = size
    height = size * 1.2  # Body height
    hood_height = width / 2  # Hood is a semicircle with radius width/2, so height is width/2

    # 1. Calculate the Y-axis shift needed to center the WHOLE graphic
    # Total Visual Height = Body Height + Hood Height
    total_height = height + hood_height

    # Y_ADJUST moves the starting point (top of the body) down so that
    # the center of the total height lands on Y=0.
    Y_ADJUST = - (total_height / 2)

    # The starting Y-coordinate for the main body's top edge is usually width/2.
    # We apply Y_ADJUST to the top edge to shift the whole image down.
    start_y = width / 2 + Y_ADJUST

    # --- 1. Base Hoodie Body ---
    t.up()
    # Start at the top-left corner with offset applied
    t.goto(-width / 2, start_y)
    t.setheading(0)
    t.down()
    draw_rectangle(t, width, height, base_color)
    t.up()

    # --- 2. Draw Pattern (Passing the calculated offset) ---
    if pattern == "stripes":
        draw_stripes(t, width, height, Y_ADJUST)
    elif pattern == "polka dots":
        draw_polka_dots(t, width, height, Y_ADJUST)
    elif pattern == "gingham":
        draw_gingham(t, width, height, Y_ADJUST)
    turtle_cleanup(t)

    # --- 3. Draw Sleeves (Applying the offset) ---
    sleeve_width = 40
    sleeve_height = height / 2
    # Sleeve Y is centered on the top half of the body, plus the shift
    sleeve_y_start = width / 2 - sleeve_height / 2 + Y_ADJUST

    # Left Sleeve
    t.goto(-width / 2 - sleeve_width, sleeve_y_start)
    t.setheading(0)
    t.down()
    draw_rectangle(t, sleeve_width, sleeve_height, base_color)

    # Right Sleeve
    t.up()
    t.goto(width / 2, sleeve_y_start)
    t.setheading(0)
    t.down()
    draw_rectangle(t, sleeve_width, sleeve_height, base_color)

    # --- 4. Draw Hood (Passing the calculated offset) ---
    draw_hood(t, width, base_color, Y_ADJUST)

    t.hideturtle()
    turtle.done()


# --- USER INPUT SECTION ---

print("Welcome to the Custom Hoodie Designer!")
print("---")

# Input and validate size
try:
    size = int(input("Enter hoodie size (100-300): "))
except ValueError:
    size = 200
    print("Invalid input for size. Using default size 200.")

if size < 100 or size > 300:
    print("Size out of range, using default size 200.")
    size = 200

# Input for base color
base_color = input("Enter hoodie base color (e.g., lightblue, lightpink, lavender): ")

# Input and validate pattern
pattern = input("Enter pattern type (**plain**, stripes, polka dots, or gingham): ").lower()
if pattern not in ["plain", "stripes", "polka dots", "gingham"]:
    print("Invalid pattern choice. Using default pattern 'plain'.")
    pattern = "plain"

print(f"\nGenerating hoodie with Size: {size}, Color: {base_color}, Pattern: {pattern}...")
draw_hoodie(size, base_color, pattern)


