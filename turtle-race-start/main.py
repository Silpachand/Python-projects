import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500,400)
colors=["red","orange","yellow","green","blue","purple"]
user_bet=turtle.textinput(title="Make your bet", prompt="Which color turtle will win the race?: ")
x=-230
y=-140
turtles=[]
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x,y)
    y+=50
    turtles.append(new_turtle)

if user_bet:
    start_race=True

while start_race:
    for i in turtles:
        if i.xcor() > 220:
            start_race = False
            if user_bet == i.pencolor():
                print(f"You've won. The winning turtle is {i.pencolor()}")
            else:
                print(f"You've lost. The winning turtle is {i.pencolor()}")
        dist=random.randint(0,10)
        i.forward(dist)

screen.exitonclick()