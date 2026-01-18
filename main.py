from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0, 0)

turtle = Turtle()
turtle.color("white")
turtle.shape("square")
turtle.penup()
turtle.shapesize(stretch_wid=5, stretch_len=1)
turtle.goto(350, 0)

def move_up():
    turtle.sety(turtle.ycor() + 20)
    screen.update()

def move_down():
    turtle.sety(turtle.ycor() - 20)
    screen.update()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.update()
screen.mainloop()
