#Write a python program to draw a 2d turtle graphics colors and shapes components. 

import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed
t.speed(2)

# Function to draw a square
def draw_square(color, size):
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Function to draw a circle
def draw_circle(color, radius):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a triangle
def draw_triangle(color, size):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Draw shapes
t.penup()
t.goto(-100, 0)
t.pendown()
draw_square("red", 100)

t.penup()
t.goto(60, 0)
t.pendown()
draw_circle("green", 50)

t.penup()
t.goto(100, 0)
t.pendown()
draw_triangle("blue", 100)

# Close the turtle graphics window when clicked
screen.exitonclick()
