from turtle import Turtle

class Snake():
    def __init__(self):
        self.segments_list = []
        
        for i in range(0,3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(-20*i,0)
            self.segments_list.append(snake_segment)

    def move(self):
        for i in range(len(self.segments_list)-1, 0, -1):
            new_x = self.segments_list[i-1].xcor() 
            new_y = self.segments_list[i-1].ycor()
            self.segments_list[i].goto(new_x, new_y)
        self.segments_list[0].forward(20)