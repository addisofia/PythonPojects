from turtle import Turtle


class Boardscore(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write_on_board()
        self.hideturtle()

    def write_on_board(self):
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 10, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 10, "bold"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write_on_board()
