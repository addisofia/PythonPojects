from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0

all_positions=[(0,0),(-20,0),(-40,0)]
move_distance=20


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]



    def create_snake(self):
        for position in all_positions:
           self.add_segments(position)


    def move(self):

        for segment_number in range(len(self.segments)-1,0,-1):
            new_x=self.segments[segment_number -1].xcor()
            new_y=self.segments[segment_number -1].ycor()
            self.segments[segment_number].goto(new_x,new_y)
        self.head.forward(move_distance)

    def add_segments(self,position):
        segment = Turtle(shape='square')
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def snake_left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)


    def snake_right(self):
        if self.head.heading() != LEFT :
           self.head.setheading(RIGHT)


