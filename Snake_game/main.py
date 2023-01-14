from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Snake Eating Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.score_count()

    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
           scoreboard.reset()
           snake.reset()
           # game_is_on = False




screen.exitonclick()