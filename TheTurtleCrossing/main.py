from turtle import Screen

from scoreboard import Scoreboard
from trafficar import Car
from player import Player
import time
import random

car_position=[(270,10),(200,150),(250,-10),(270,-90),(250,-170),(230,-100)]
traffic=[]
new_y=[-150,-90,0,100,200]


screen=Screen()
screen.setup(width=600,height=500)
screen.bgcolor('white')
screen.title("turtle crossing the road")
screen.tracer(0)


player=Player((0,-230))
scoreboard=Scoreboard()

# create a lot of object car and stock in the traffic list

for position in car_position:
    new_car = Car(position)
    traffic.append(new_car)

#move the player by the keyborad

screen.listen()
screen.onkey(player.move_player,'Up')




speed_score=0.5
game_on=True
while game_on:
    time.sleep(speed_score)
    screen.update()
    #player.move_player()

    for car in traffic:
        car.moving()
# if the car arrive to the end so they start from the beginner
        if car.xcor() <-300:
            car.goto(300,random.choice(new_y))

# detect colision with car
        if player.distance(car) < 20 :
            scoreboard.game_over()
            game_on = False

# add car to the list of car if random is equal at 1

    if random.randint(1,6)==1:
        new_car=Car((300,random.choice(new_y)))
        traffic.append(new_car)

#arrive to the boarder , so you will start from the beginner and increase score
    if player.ycor()>200:
        player.goto(0,-230)
        scoreboard.increase()
        speed_score*=0.9














screen.exitonclick()
