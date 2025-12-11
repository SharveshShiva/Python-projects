from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
NUM = 3

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        number = NUM
        for i in range(number):
            self.add_segment(number)

    def add_segment(self,position):
        x = -40
        y = 0
        doug = Turtle()
        doug.shape("square")
        doug.color("white")
        doug.penup()
        doug.goto(x, y)
        x = x + 20
        self.segment.append(doug)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            x = self.segment[i - 1].xcor()
            y = self.segment[i - 1].ycor()
            self.segment[i].goto(x, y)
        self.head.fd(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)