import turtle
import random


# --- Helper Functions ---

def turtle_cleanup(t):
    """Lifts the pen, hides the turtle, and resets state after drawing."""
    t.up()
    t.hideturtle()
    t.setheading(0)
    t.goto(0, 0)


def draw_rectangle(t, width, height, color):
    """Draws a filled rectangle for the body and sleeves."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def draw_hood(t, width, color, y_offset):
    """Draws the hood oriented to the RIGHT, with the semicircular part facing UP."""

    t.up()
    # 1. Move to the absolute start of the arc (TOP-CENTER of the main hoodie body)
    t.goto(0, width / 2 + y_offset)
    t.setheading(90)  # Face up

    # 2. Move RIGHT with pen UP to the *starting point* of the semi-circle
    t.right(90)
    t.forward(width / 2)  # Move right to the edge of the hood

    # 3. Start drawing the arc
    t.down()  # Pen down ONLY for the arc

    t.fillcolor(color)
    t.begin_fill()

    t.left(90)
    t.circle(width / 2, 180)  # Draw the semi-circle clockwise

    t.end_fill()

    # 4. Cleanup: Move back to the body's top edge (the base of the hood) with pen UP
    t.up()
    t.goto(0, width / 2 + y_offset)  # Jump back to the center line

    turtle_cleanup(t)


def draw_stripes(t, size, height, y_offset):
    """Draws vertical pastel stripes, applying the offset."""
    t.width(1)
    stripe_width = size / 10
    start_y = size / 2 + y_offset

    # Define colors for the pattern
    stripe_colors = ["#FADADD", "#B0E0E6", "#E6E6FA"]

    for i in range(10):  # Loop for stripes
        t.up()
        # Position for the stripe's top-left corner
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
    """Draws polka dots pattern, applying the offset."""
    t.up()
    dot_colors = ["lightpink", "lightyellow", "lightgreen", "lightblue"]

    x_range = range(-int(size / 2) + 15, int(size / 2), 30)  # Loop for X grid
    # Loop for Y grid, adjusting starting and ending points by offset
    y_range = range(int(size / 2) - 15 + y_offset, int(size / 2) - int(height) + y_offset, -30)

    for x in x_range:
        for y in y_range:  # Nested loops create the dot grid
            t.goto(x, y)
            t.dot(10, random.choice(dot_colors))
    turtle_cleanup(t)


def draw_gingham(t, size, height, y_offset):
    """Draws gingham (checkered) pattern, applying the offset."""
    square_size = 20
    colors = ["#FADADD", "#E6E6FA"]

    num_x = int(size // square_size)
    num_y = int(height // square_size)

    for i in range(num_x):
        for j in range(num_y):  # Nested loops for checkered pattern
            t.up()
            # Position for the square's top-left corner
            t.goto(-size / 2 + i * square_size, size / 2 - j * square_size + y_offset)
            t.setheading(0)
            t.down()

            t.fillcolor(colors[(i + j) % 2])  # Conditional color choice
            t.begin_fill()

            for _ in range(4):
                t.forward(square_size)
                t.right(90)
            t.end_fill()
    turtle_cleanup(t)


# --- Main Drawing Function ---

def draw_hoodie(size, base_color, pattern):
    """Main function to draw the complete hoodie."""
    screen = turtle.Screen()
    screen.title("Custom Hoodie Design")
    screen.setup(width=size + 150, height=size * 2)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    width = size
    height = size * 1.2

    # VISUAL CENTERING ADJUSTMENT: Shifts the entire drawing UP
    Y_OFFSET = 100

    start_y = width / 2 + Y_OFFSET  # Calculated starting Y-position

    # --- 1. Base Hoodie Body ---
    t.up()
    t.goto(-width / 2, start_y)
    t.setheading(0)
    t.down()
    draw_rectangle(t, width, height, base_color)
    t.up()

    # --- 2. Draw Pattern ---
    if pattern == "stripes":
        draw_stripes(t, width, height, Y_OFFSET)
    elif pattern == "polka dots":
        draw_polka_dots(t, width, height, Y_OFFSET)
    elif pattern == "gingham":
        draw_gingham(t, width, height, Y_OFFSET)

    # --- 3. Draw Sleeves (Applying the offset) ---
    sleeve_width = 40
    sleeve_height = height / 2
    sleeve_y_start = width / 2 - sleeve_height / 2 + Y_OFFSET

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

    # --- 4. Draw Hood (Right-oriented and positioned correctly) ---
    draw_hood(t, width, base_color, Y_OFFSET)

    turtle.done()


# --- USER INPUT SECTION (Using variables and conditionals) ---

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


