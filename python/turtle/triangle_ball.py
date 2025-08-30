import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')
t.penup
t.goto(0,200)
t.pendown
t.speed(0)
x=0
y=0

for i in range(10000):
    t.forward(x)
    t.right(y)
    x+=2
    y+=0.5

turtle.done()