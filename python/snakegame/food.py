import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,
                       stretch_len=0.5)  # turtle is 20X20,we're making food turtle to be 0.5 times: 10X10
        self.color("green")
        self.penup()  # SO that it doesn't draw when we shift food's position
        self.speed("fastest")

        self.new_pos()

    def new_pos(self):
        random_pos = (random.randint(-300, 300), random.randint(-300, 300))
        self.goto(random_pos)
