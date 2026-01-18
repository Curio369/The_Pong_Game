from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.start_move_up, "Up")
screen.onkeyrelease(r_paddle.stop_move, "Up")
screen.onkeypress(r_paddle.start_move_down, "Down")
screen.onkeyrelease(r_paddle.stop_move, "Down")
screen.onkeypress(l_paddle.start_move_up, "w")
screen.onkeyrelease(l_paddle.stop_move, "w")
screen.onkeypress(l_paddle.start_move_down, "s")
screen.onkeyrelease(l_paddle.stop_move, "s")

game_is_on = True
screen.update()

while game_is_on:
    r_paddle.update()
    l_paddle.update()
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.mainloop()
