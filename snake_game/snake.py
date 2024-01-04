from turtle import Turtle

STARTING_POSITION = ((0,0),(-20,0),(-40,0))
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.controls = {
            "Left" : self.left_key,
            "Right" : self.right_key,
            "Up" : self.up_key,
            "Down" : self.down_key,
            }
        self.head = self.segments_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments_list.append(snake_segment)

    def move(self):
        for i in range(len(self.segments_list)-1, 0, -1):
            new_x = self.segments_list[i-1].xcor() 
            new_y = self.segments_list[i-1].ycor()
            self.segments_list[i].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)
    
    def left_key(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_key(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up_key(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_key(self):
        if self.head.heading() != UP:
            self.head.setheading(270)