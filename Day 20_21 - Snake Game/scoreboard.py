from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",16,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.pendown()
        self.score_count = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score_count}",align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGN, font=FONT)
    def increase_score(self):
        self.score_count = self.score_count + 1
        self.clear()
        self.update_score()




