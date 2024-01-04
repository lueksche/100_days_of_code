# Imorting needed packages

from turtle import Screen, Turtle
from snake import Snake
from time import sleep

# Setting up screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initiating snake object

snake = Snake()

# Listening events

# Running the game
screen.listen()

for arrow_key, direction in snake.controls.items():
    screen.onkey(key=arrow_key, fun=direction)

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()