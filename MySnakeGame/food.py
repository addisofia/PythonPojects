import random
from turtle import Turtle

from snake import all_positions


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("blue")
        self.penup()
        self.refresh()



    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position,y_position)











