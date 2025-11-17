from turtle import Screen,Turtle



class Boardscore(Turtle) :
    def __init__(self,position):
        super().__init__()
        self.position=position
        self.score=0
        self.color('white')
        self.penup()
        self.goto(self.position)
        self.write_score()
        self.hideturtle()


    def write_score(self):
        self.write(f"{self.score}",font=("Arial", 20, "bold"))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 10, "bold"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write_score()



