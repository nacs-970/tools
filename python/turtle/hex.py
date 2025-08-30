import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')
t.speed(0)

for i in range(550):
    t.forward(i)
    t.right(59)

turtle.done()