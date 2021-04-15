from turtle import Turtle


class Ball(Turtle):

    #main ball settings
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.5 #origionally put in 0.9 but that was warp speed on my machine, slowed it way down for testing and settled on 0.5 as a nice go between.
        self.y_move = 0.5
        self.move_speed = 0.1

    #moving ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    #bouncy ball
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
