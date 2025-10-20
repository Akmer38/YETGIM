import turtle

pencere = turtle.Screen()

pencere.bgcolor(   "white")
pencere.title("turtl ile çizim")

kalem = turtle.Turtle()
kalem.pensize(4)
kalem.color("green")


for i in range(10):
    kalem.forward(40*(i+1))
    kalem.right(90)

turtle.done()