from turtle import Turtle
from ball import Ball
import random


class Food():
    def __init__(self):
        self.normal_ball = Ball('white', 0.5)
        self.bonus_ball = Ball('green', 1)
        self.food_count = 0
        self.show_normal_ball()

    def eat_ball(self):
        """Refresh the food and places it on a random place on the screen"""
        if self.ball == self.normal_ball:
            self.food_count += 1
            
        if self.food_count % 5 == 0 and self.ball == self.normal_ball:  
            self.show_bonus_ball()
        else:
            self.show_normal_ball()
            
        self.ball.refresh()

        
    def food_reset(self):
        self.food_count = 0
        self.show_normal_ball()

    def show_normal_ball(self):
        self.bonus_ball.hideturtle()
        self.normal_ball.showturtle()
        self.ball = self.normal_ball
        
    def show_bonus_ball(self):
        self.normal_ball.hideturtle()
        self.bonus_ball.showturtle()
        self.ball = self.bonus_ball