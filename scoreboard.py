from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Update the scoreboard after successfully eating a food """
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Shows game over whenever the game is over"""
        self.goto(0, 0)
        self.write(f"GAME OVER🥲", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ Update the scoreboard after successfully eating a food """
        self.score += 1
        self.clear()
        self.update_scoreboard()
