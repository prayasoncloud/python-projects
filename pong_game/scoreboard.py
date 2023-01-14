from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_point =0
        self.r_point = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_point, align="center", font=("courier", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_point, align="center", font=("courier", 30, "normal"))

    def l_score(self):
        self.clear()
        self.l_point += 1
        self.update_scoreboard()

    def r_score(self):
        self.clear()
        self.r_point += 1
        self.update_scoreboard()
