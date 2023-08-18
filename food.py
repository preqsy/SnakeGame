from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.food_count = 0
        self.refresh()

    def refresh(self):
        """Refresh the food and places it on a random place on the screen"""
        self.food_count += 1
        randomx = random.randint(-250, 250)
        randomy = random.randint(-250, 250)

        self.goto(randomx, randomy)

    def bonus(self):
        """Generates a big bonus food and place it on a random place on the screen"""
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('green')
        randomx = random.randint(-250, 250)
        randomy = random.randint(-250, 250)
        self.goto(randomx, randomy)
