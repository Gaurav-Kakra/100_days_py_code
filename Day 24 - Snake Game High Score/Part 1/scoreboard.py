from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        #with open("C:/Users/admin/Desktop/Python codes/Udemy Python AY/Day 24/Part 1/data.txt",mode='r') as file:
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            #with open("C:/Users/admin/Desktop/Python codes/Udemy Python AY/Day 24/Part 1/data.txt",mode='w') as file:
            with open("data.txt",mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
