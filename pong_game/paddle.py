from turtle import Turtle

MOVING_DISTANCE = 20
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.controls_directory = {}
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def up_key(self):
        if self.ycor() < 250:
            new_ycor = self.ycor() + MOVING_DISTANCE
            self.goto(self.xcor(),new_ycor)
    
    def down_key(self):
        if self.ycor() > - 250:
            new_ycor = self.ycor() - MOVING_DISTANCE
            self.goto(self.xcor(),new_ycor)

    def initiate_paddle(self, side):
        self.shape("square")
        self.penup()
        self.color("white")
    
        if side == "left":
            self.goto(-350,0)
            self.controls_directory = {'w' : self.up_key,
                                         's' : self.down_key,
            }

        else:
            self.goto(350,0)
            self.controls_directory = {"Up" : self.up_key,
                                         "Down" : self.down_key,
            }