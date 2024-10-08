#Week2: Day 5 - Draw a Picture with House Function
#Melissa Usher

import turtle

def square(len):
    for i in range (4):
        turtle.forward(len)
        turtle.right(90)

def triangle(len):
    for i in range (3):
        turtle.forward(len)
        turtle.left(120)

def house(len):
    square(len)
    triangle(len)

def main():
    turtle.speed(0)
    turtle.color("green")
    house(100)
    turtle.color("gray")
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    house(50)
    turtle.color("red")
    turtle.penup()
    turtle. backward(275)
    turtle.pendown()
    house(75)

main()

turtle.Screen().exitonclick()
