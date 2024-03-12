from turtle import Turtle

COLOR = "white"

class Line(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(xcor,300)
        self.display_line(xcor)
    
    def display_line(self,xcor):
        self.pencolor("white")
        self.pensize(5)
        while self.ycor() > -300:
            self.setheading(270)
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
    
    def update(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()

        