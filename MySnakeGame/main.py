from turtle import Screen
import time
from snake import Snake
from food import Food
from boardscore import Boardscore





screen=Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("MY THE SNAKE GAME")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.snake_right,'Right')
screen.onkey(snake.snake_left,'Left')

board_score=Boardscore()
food=Food()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food) <20:
        food.refresh()
        snake.extend()
        board_score.increase()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            board_score.game_over()
            game_is_on=False


    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_is_on=False
        board_score.game_over()


screen.exitonclick()








