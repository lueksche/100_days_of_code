from turtle import Turtle

ALIGNMENT = "center"
FONT_TUPLE = ('Courier', '24', 'nomral')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.display_scoreboard()
    
    def display_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT_TUPLE)
    
    def update(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()
        