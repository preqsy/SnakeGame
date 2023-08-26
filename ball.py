from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, color, size):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=size, stretch_wid=size)
        self.color(color)
        self.speed('fastest')
        self.refresh()
        self.hideturtle()

    def refresh(self):
        """Refresh the food and places it on a random place on the screen"""
        randomx = random.randint(-250, 250)
        randomy = random.randint(-250, 250)

        self.goto(randomx, randomy)
