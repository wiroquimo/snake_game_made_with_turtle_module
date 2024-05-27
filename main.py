#!/usr/bin/env python3

from turtle import Turtle, Screen

# import time
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AliceBlue")
screen.title("my snake game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
serpent = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True
sleep_speed = 0.1
screen.listen()
screen.onkey(serpent.up, "Up")
screen.onkey(serpent.down, "Down")
screen.onkey(serpent.left, "Left")
screen.onkey(serpent.right, "Right")

while game_is_on:
    screen.update()
    sleep(sleep_speed)
    serpent.move()
    # detect collision with food
    if serpent.segments[0].distance(food) < 15:
        food.refresh()
        serpent.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if (
        serpent.segments[0].xcor() > 280
        or serpent.segments[0].xcor() < -280
        or serpent.segments[0].ycor() > 280
        or serpent.segments[0].ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        sleep(5)
        screen.bye()

screen.exitonclick()
