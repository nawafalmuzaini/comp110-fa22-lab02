"""
Module: name_drawer
Sep.18 2022
A program to draw a name using one (or more) turtles.

Authors:
1) Nawaf- nalmuzaini@sandiego.edu
09/17/2022

"""
#importing turtle
import turtle 
t=turtle.Turtle()

#asking user to type name
name = input("Type name NAWAF")

#if loop that executes when the user types my name
if name == "NAWAF":
#drawing letter N
 t.pensize(15)         #setting pensize to 15 so drawing is clearly visible
t.color("white")
t.setposition(-350,0)   #setting position to start the drawing from the left
t.color("blue")
t.right(90)
t.forward(120)
t.backward(120)
t.left(40)
t.forward(155)
t.left(139)
t.forward(120)
t.penup()

#drawing letter A
t.goto(-225,-100)
t.right(90)
t.pendown()
t.pencolor("red")
t.left(75)
t.forward(100)
t.right(145)
t.forward(100)
t.bk(40)
t.right(107)
t.forward(35)
t.right(108)
t.forward(52)
t.penup()

#drawing letter W
t.goto(-150,0) 
t.pendown()
t.pensize(15)
t.pencolor("blue")
t.right(140)
t.forward(100)
t.left(130)
t.forward(100)
t.right(120)
t.forward(100)
t.left(130)
t.forward(100)
t.penup()

#drawing letter A
t.goto(30,-70)
t.pendown()
t.right(80)
t.pendown()
t.pencolor("red")
t.left(75)
t.forward(100)
t.right(145)
t.forward(100)
t.bk(40)
t.right(107)
t.forward(35)
t.right(108)
t.forward(52)
t.penup()

#drawing letter F
t.setpos(120,50) 
t.pendown()
t.pensize(15)
t.pencolor("blue")
t.right(70)
t.forward(80)
t.backward(80)
t.right(90)
t.forward(100)
t.left(90)
t.forward(80)
t.backward(80)
t.right(90)
t.forward(80)

turtle.Screen().exitonclick()
