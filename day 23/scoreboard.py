from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoretable()

    def update_scoretable(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f"Level: {self.score}", align='left', font=FONT)
        self.score += 1

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
