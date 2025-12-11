from turtle import Turtle
FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT, move=False)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT, move=False)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT, move=False)

