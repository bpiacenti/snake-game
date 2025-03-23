from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")

class Scoreboard(Turtle):
    """Functions related to score at top of screen"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 270)

    def score_display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def score_point(self):
        self.score += 1