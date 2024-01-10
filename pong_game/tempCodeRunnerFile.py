from turtle import Turtle, Screen

STARTING_POSITION_LEFT = ((-480,0),(-480,20),(-480,-20))
STARTING_POSITION_RIGHT = ((480,0),(480,20),(480,-20))
MOVING_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self):
        self.starting_position = []
        self.paddle_sgements_list = []
        self.controls_directory = {}
    
    def up_key(self):
        for segment in self.paddle_sgements_list:
            self.setheading(UP)
            segment.forward(MOVING_DISTANCE)
    
    def down_key(self):
        for segment in self.paddle_sgements_list:
            self.setheading(DOWN)
            segment.forward(20)
    
    def initiate_paddle(self, side):
        if side == "left":
            for position in STARTING_POSITION_LEFT: 
                self.add_segments(position)
            self.controls_directory["W"] = self.up_key
            self.controls_directory["A"] = self.down_key

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


#Initiating screen

screen = Screen()

#Setting up screen

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

test = Paddle()
test.color("white")
test.forward(20)


screen.exitonclick()
    