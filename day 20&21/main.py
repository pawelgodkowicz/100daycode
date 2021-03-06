from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

img = "gifrab.gif"

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Jungle Python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)

    snake.move()

    # food colision detection
    if snake.head.distance(food) < 15:
        food.resurection()
        snake.extend()
        scoreboard.increase_score()

    # wall colision detection
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_the_scoreboard()
        snake.reset()
    # tail colision detection
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_the_scoreboard()
            snake.reset()

screen.exitonclick()
