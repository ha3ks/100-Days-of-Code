from turtle import Turtle, Screen

turty = Turtle()
screen = Screen()


def move_forwards():
    turty.forward(10)

def move_backwards():
    turty.backward(10)

def turn_left():
    new_heading = turty.heading() + 10
    turty.setheading(new_heading)

def turn_right():
    new_heading = turty.heading() - 10
    turty.setheading(new_heading)

def clear():
    turty.clear()
    turty.penup()
    turty.home()
    turty.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
