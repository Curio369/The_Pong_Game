from turtle import Turtle
import main

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)
        main.screen.update()

    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
        main.screen.update()

