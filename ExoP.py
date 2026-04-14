import turtle

#Screen Title
turtle.title('Exo Planet')

#Initializing Turtle Graphics
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('Black')
t.pencolor('Blue')

#Logic
x = 0
y = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while True:
    t.forward(x)
    t.right(y)
    x += 3
    y += 1
    if y == 210:
        break
    t.hideturtle()
turtle.done()