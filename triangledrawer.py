import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(2)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        drawer.forward(size)
        drawer.left(120)

# Draw a triangle with side length 100
draw_triangle(100)

# Hide the turtle and display the window
drawer.hideturtle()
wn.mainloop()
