from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.movement = 0

    def start_move_up(self):
        self.movement = 1

    def start_move_down(self):
        self.movement = -1

    def stop_move(self):
        self.movement = 0

    def update(self):
        if self.movement != 0:
            new_y = self.ycor() + 20 * self.movement
            if -280 < new_y < 280:
                self.sety(new_y)
