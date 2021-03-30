#This is coded for use on the Reeborgs World Maze Escape, written in VIM while also watching the instructional video with transparancy added so I can work and play at the same time like an absolute badman!!

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#debugging when nothing is on the right
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

