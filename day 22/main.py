from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoretable import Scoretable
import time

screen = Screen()
screen.title("PONG")
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

game_is_on = True

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoretable = Scoretable()
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.goUp, "Up")
screen.onkeypress(r_paddle.goDown, "Down")
screen.onkeypress(l_paddle.goUp, "w")
screen.onkeypress(l_paddle.goDown, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.rolling()

    # collision with right wall
    if ball.xcor() > 380:
        ball.reset_ball()
        scoretable.l_point()

    # collision with left wall
    if ball.xcor() < -380:
        ball.reset_ball()
        scoretable.r_point()

    # collision with horizontal lines
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncing_y()

    # collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouncing_x()

    # display winner
    if scoretable.l_score == 10:
        scoretable.gameover("Player Left")
        game_is_on = False

    elif scoretable.r_score == 10:
        scoretable.gameover("Player Right")
        game_is_on = False

screen.exitonclick()
