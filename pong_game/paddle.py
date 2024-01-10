from turtle import Turtle, Screen

STARTING_POSITION_LEFT = ((-480,20),(-480,0),(-480,-20))
STARTING_POSITION_RIGHT = ((480,20),(480,0),(480,-20))
MOVING_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self):
        self.starting_position = []
        self.paddle_sgements_list = []
        self.controls_directory = {}
    
    def up_key(self):
        if self.paddle_sgements_list[0].ycor() < 280:
            for segment in self.paddle_sgements_list:
                segment.setheading(UP)
                segment.forward(MOVING_DISTANCE)
        
    def down_key(self):
       if self.paddle_sgements_list[2].ycor() > -280:
        for segment in self.paddle_sgements_list:
                segment.setheading(DOWN)
                segment.forward(20)
    
    def initiate_paddle(self, side):
        if side == "left":
            for position in STARTING_POSITION_LEFT: 
                self.add_segments(position)
            self.controls_directory["W"] = self.up_key
            self.controls_directory["S"] = self.down_key

        else:
            for position in STARTING_POSITION_RIGHT:
                self.add_segments(position)
            self.controls_directory["Up"] = self.up_key
            self.controls_directory["Down"] = self.down_key
            

    def add_segments(self, position):        
        paddle_segment = Turtle(shape="square")
        paddle_segment.penup()
        paddle_segment.color("white")
        paddle_segment.goto(position)
        self.paddle_sgements_list.append(paddle_segment)