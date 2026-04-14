import turtle

screen = turtle.Screen()
screen.title("3 Turtle Shapes")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)

# --- Circle ---
t.penup()
t.goto(-200, 0)
t.pendown()
t.pencolor("green")
t.circle(80)

# --- Square ---
t.penup()
t.goto(-30, -40)
t.pendown()
t.pencolor("blue")
for _ in range(4):
    t.forward(100)
    t.left(90)

# --- Triangle ---
t.penup()
t.goto(180, -40)
t.pendown()
t.pencolor("orange")
for _ in range(3):
    t.forward(100)
    t.left(120)

t.hideturtle()
turtle.done()