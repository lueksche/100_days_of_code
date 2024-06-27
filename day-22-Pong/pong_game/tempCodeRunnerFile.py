from turtle import Turtle

MOVING_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        self.controls_directory = {}
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def up_key(self):
        if self.ycor() < 330:
            new_ycor = self.ycor() + MOVING_DISTANCE
            self.goto(self.xcor(),new_ycor)
    
    def down_key(self):
        if self.ycor() > - 330:
            new_ycor = self.ycor() - MOVING_DISTANCE
            self.goto(self.xcor(),new_ycor)

    def initiate_paddle(self, side):
        paddle = Turtle(shape="square")
        paddle.penup()
        paddle.color("white")
    
        if side == "left":
            self.goto(-350,0)
            self.controls_directory["W"] = self.up_key
            self.controls_directory["S"] = self.down_key

        else:
            self.goto(350,0)
            self.controls_directory["Up"] = self.up_key
            self.controls_directory["Down"] = self.down_key

paddle = Paddle()
paddle.initiate_paddle("left")
