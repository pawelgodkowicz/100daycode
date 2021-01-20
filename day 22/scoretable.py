from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoretable(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoretable()

    def update_scoretable(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.l_score, align='center', font=("Arial", 60, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, align='center', font=("Arial", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoretable()

    def r_point(self):
        self.r_score += 1
        self.update_scoretable()

    def gameover(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} WIN !", align=ALIGNMENT, font=FONT)
