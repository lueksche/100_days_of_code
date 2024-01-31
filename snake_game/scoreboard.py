from turtle import Turtle

ALIGNMENT = "center"
FONT_TUPLE = ('Courier', '24', 'bold')
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self._display_scoreboard()
    
    def _display_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT_TUPLE)
    
    def increase_score(self):
        self.score += 1
        self._display_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_TUPLE)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self._display_scoreboard()