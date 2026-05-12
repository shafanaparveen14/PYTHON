import turtle
import math
# Screen setup
screen =turtle.Screen()
screen.bgcolor("orange")
#Turtle for big circle
big=turtle.Turtle()
big.hideturtle()
big.speed(0)
#Draw big circle
big.penup()
big.goto(0, -100)
big.pendown()
big.circle(100)
#Turtle for small circle
small=turtle.Turtle()
small.shape("circle")
small.color("blue")
small.penup()
#Elliptical motion
a=150#horizontal radius
b=80#Vertical radius
for angle in range(0,360,2):
    x=a*math.cos(math.radians(angle))
    y=b*math.sin(math.radians(angle))
    small.goto(x,y)
turtle.done()
