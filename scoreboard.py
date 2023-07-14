from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_level()

    def update_level(self):
        self.goto(-270, 260)
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", "center", font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER!", "center", font=FONT)


