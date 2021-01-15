from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(900, 400)
user_bet = screen.textinput(title="Race bet", prompt="Which turtle will win the race? Type color:")


def birth_of_turtle(colors, y_position):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(430, y_position[i])
    turtle.setheading(180)
    turtles.append(turtle)


colors = ["green", "red", "yellow", "blue", "orange", "purple"]
y_position = [-75, -45, -15, 15, 45, 75]
turtles = []

for i in range(0, 6):
    birth_of_turtle(colors, y_position)

race_on = False

if user_bet in colors:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() <= -430:
            race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle won the race!")
            else:
                print(f"You've lose! The {win_color} turtle won the race!")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
