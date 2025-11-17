from turtle import Turtle
import random



class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('turtle')
        self.position=position
        self.color('black')
        self.penup()
        self.goto(position)
        self.setheading(90)


    def move_player(self):
        self.forward(20)
        #new_y=self.ycor()+20
        #self.goto((self.xcor(),new_y))


