import turtle

from Tools.demo.spreadsheet import center

ALIGNMENT= "center"
FONT= ("Courier", 17, "normal")

class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=321)
        self.pendown()
        self.write(arg=f"Score :: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score :: {self.score}", align="center", font=("Arial", 21, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 100)
        self.pendown()
        self.write(arg="GAME OVER", align=ALIGNMENT, font=("Courier", 51, "normal"))



