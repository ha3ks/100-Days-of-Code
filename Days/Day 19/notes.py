#Day 19

#Two projects today, a turtle race and an etch-a-sketch,, this is awesome!

#Event Listeners
#these pickup on when the user does something on the keyboard i.e. presses an arrow

#will use the onkey.event

from turtle import Turtle, Screen

turty = Turtle()
screen = Screen()

def move_forwards():
    turty.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()  


