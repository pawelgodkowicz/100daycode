# Picture downloaded from:
# https://i.guim.co.uk/img/static/sys-images/Arts/Arts_/Pictures/2012/1/13/1326458117290/Addictive---detail-of-Dam-007.jpg?width=300&quality=45&auto=format&fit=max&dpr=2&s=f7fefcb3bd79637427928210e67e6e26

import colorgram
import turtle as t
import random

colors = colorgram.extract('hirst.jpg', 20)
colores = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]

screen = t.Screen()
root = screen._root
root.iconbitmap("icon.ico")
screen.title("Drawing Hirst's picture")

t.colormode(255)
t.screensize(400, 400)

trt = t.Turtle()

trt.speed(0)
trt.penup()
trt.hideturtle()

trt.setheading(225)
trt.forward(353)
trt.setheading(0)

dots_nr = 100

for counter in range(1, dots_nr + 1):
    trt.dot(30, random.choice(colores))
    trt.forward(50)
    if counter % 10 == 0:
        trt.setheading(90)
        trt.forward(50)
        trt.setheading(180)
        trt.forward(500)
        trt.setheading(0)

screen.exitonclick()