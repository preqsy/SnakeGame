from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title("My Snake game")
snake = Snake()
scoreboard = Scoreboard()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
# snake.create_snake()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detects a collide with food
    if snake.head.distance(food.ball) < 15:   
        snake.extend()
        scoreboard.increase_score()
        food.eat_ball()
        
    # Detects a collision with the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        food.food_reset()

    # Detects collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            food.food_reset()
# create a function that adds the bonus
# make the bonus appear everytime the scores in divisible by 5, then continue
screen.exitonclick()
