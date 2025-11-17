from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2)
        self.position=position
        self.choose_color()
        self.penup()
        self.goto(position)
        self.setheading(180)
        self.moving()





    def choose_color(self):
        list_color=['blue','red','green','black','yellow','pink']
        self.color(random.choice(list_color))

    def moving(self):
        self.forward(20)








