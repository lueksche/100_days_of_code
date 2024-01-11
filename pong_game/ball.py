from turtle import Turtle
import random

MOVING_DISTANCE = 20
TURNS_TO_INCREASE_SPEED = 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.out_of_bounds_counter =  1
        self.move_speed = 0.1

    def serve(self, direction):
        self.goto(0,0)
        if direction == "right":
            random_direction = random.choice([x for x in range(1,360) if x not in range(45,315)])
            self.setheading(random_direction)
        else:
            random_direction = random.choice([x for x in range(135,225) if x != 180])
            self.setheading(random_direction)

    def move(self):
        self.forward(MOVING_DISTANCE)
    
    def collision_paddle(self, obstacle):
        if self.distance(obstacle) < 50 and abs(self.xcor()) > 340:
            new_direction = 180 - self.heading()
            self.setheading(new_direction)
            self.move_speed *= 0.9

    def collision_wall(self):
        if abs(self.ycor()) > 280:
            new_direction = self.heading() * -1
            self.setheading(new_direction)

    def out_of_bounds_left(self):
        if self.xcor() < - 360:
            self.out_of_bounds_counter += 1
            self.move_speed = 0.1
            self.serve("right")
            
            return True
        
    def out_of_bounds_right(self):
        if self.xcor() > 360:
            self.out_of_bounds_counter += 1
            self.move_speed = 0.1
            self.serve("left")
            return True
