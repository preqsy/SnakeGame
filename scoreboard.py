from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0      
        self.color('white')
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Update the scoreboard after successfully eating a food """
        self.clear()
        self.write(f"Score:{self.score} HighScore:{self.highscore}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """ Update the scoreboard after successfully eating a food """
        self.score += 1
        self.update_scoreboard()
