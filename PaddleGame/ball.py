from turtle import Turtle



class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color('white')
        self.speed('slow')
        self.penup()
        self.xmove=5
        self.ymove=5
        self.move_speed=0.1



    def move_ball(self):
        newx=self.xcor()+ self.xmove
        newy=self.ycor() +self.ymove
        self.goto(newx,newy)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *=0.9

    def reset_position(self):
        self.move_speed=0.1
        self.goto(0, 0)
        self.bounce_x()

