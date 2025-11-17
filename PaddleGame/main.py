import time
from turtle import Screen

from boardscore import Boardscore

from paddle import Paddle
from ball import Ball
position=[(-350,0),(350,0)]
all_position=[(-340,280),(-340,200),(-340,100)]


screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

pad1=Paddle(position[0])
pad2=Paddle(position[1])
ball=Ball()
board_score1=Boardscore((-50,250))
board_score2=Boardscore((50,250))

screen.listen()
screen.onkey(pad1.move_up,'s')
screen.onkey(pad1.move_down,'w')

screen.onkey(pad2.move_up,'Up')
screen.onkey(pad2.move_down,'Down')



game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()


    if ball.distance(pad2) <50 and ball.xcor()> 320:
        ball.bounce_x()


    if ball.distance(pad1) <50 and ball.xcor()< -320:
        ball.bounce_x()


    if ball.xcor() >=400   :
        board_score1.increase()
        ball.reset_position()

    if ball.xcor() <=-400:
        board_score2.increase()
        ball.reset_position()




















screen.exitonclick()
