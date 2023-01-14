from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.write("Game Over", font=("Arial", 20, "normal"), align="center")
