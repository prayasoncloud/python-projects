from turtle import Turtle, Screen

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt", mode= "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        # with open("data.txt", mode="r") as file:
        #     self.high_score = int(file.read())
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))


    def score_count(self):
        self.score += 1
        self.update_score()
