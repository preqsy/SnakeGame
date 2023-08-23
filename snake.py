from turtle import Turtle, Screen
import time
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        print(len(self.segments))
        self.head = self.segments[0]

    def create_snake(self):
        """ Creates The Snake """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Creates the snake"""
        new_segment = Turtle(shape='square')
        new_segment.color('red')
        new_segment.penup()
        new_segment.goto(position)
        new_segment.penup()
        self.segments.append(new_segment)

    def extend(self):
        """ Extends the snake length """
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            time.sleep(0.1)
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

