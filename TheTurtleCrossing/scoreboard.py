from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(-290,195)
        self.hideturtle()
        self.write(f"level:{self.score}",font=("Arial",15,"bold"))




    def write_score(self):
        self.write(f"level:{self.score}",font=("Arial",15,"bold"))


    def increase(self):
        self.score+=1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.write("GAME OVER",move=False,align="center",font=("Arial",15,"bold"))
        self.goto(0,0)



