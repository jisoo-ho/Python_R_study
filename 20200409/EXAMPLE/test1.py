import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(3)
t.width(3)
t.shape("turtle")
length=10

while length<500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right (89)
    length += 5

