from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_coordinate = randint(-280, 280)
        random_y_coordinate = randint(-280, 280)
        self.goto(random_x_coordinate, random_y_coordinate)