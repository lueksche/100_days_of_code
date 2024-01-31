from turtle import Turtle

ALIGNMENT = "center"
FONT_TUPLE = ('Courier', '80', 'bold')
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(position)
        self.score = 0
        self.display_scoreboard()
    
    def display_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT_TUPLE)
    
    def update(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()

        