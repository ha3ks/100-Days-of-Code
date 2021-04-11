#Day 18

#Turtle & the Graphical User Interface (GUI)
#Basically using the turtle to make million dollar art/NFTs.. good times!

######## Challenge 1 - Draw a Square ############
import turtle as t

turty = t.Turtle()

for _ in range(4):
    turty.forward(100)
    turty.left(90)



########### Challenge 2 - Draw a Dashed Line ########
import turtle as t

turty = t.Turtle()

for _ in range(15):
    turty.forward(10)
    turty.penup()
    turty.forward(10)
    turty.pendown()




########### Challenge 3 - Draw Shapes ########
import turtle as t
import random

turty = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turty.forward(100)
        turty.right(angle)

for shape_side_n in range(3, 10):
    turty.color(random.choice(colours))
    draw_shape(shape_side_n)



########### Challenge 4 - Random Walk ########
import turtle as t
import random

turty = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turty.pensize(15)
turty.speed("fastest")

for _ in range(200):
    turty.color(random.choice(colours))
    turty.forward(30)
    turty.setheading(random.choice(directions))




########### Challenge 5 - Spirograph ########
import turtle as t
import random

turty = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turty.color(random_color())
        turty.circle(100)
        turty.setheading(turty.heading() + size_of_gap)

draw_spirograph(5)

