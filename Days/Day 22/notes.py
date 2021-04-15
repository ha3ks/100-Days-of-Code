#Day 22

#making Pong, the game!!!

#breaking project into 8 seperate segments

#Tasks
#Create the screen
#Create and move a paddle
#Create another paddle
#create a ball and make it move
#detect wall collision and bounce
#detect collision with a paddle
#detect when paddle misses a ball
#keep score



#Added screen to main.py (going with that standardized naming for this project)

#Added paddle code to main.py
#Due to needing 2 paddles decided to make a seperate paddle.py to import the settings for a paddle and clean up the code in main.py

#That worked out as course also indicates that you would import a paddle class, as the left paddle is different to right need to pass it the coordiantes to start the game.
#Edited the code to allow W and S for up and down while up arrow and down arrow still do the right paddle!

#Detecting collison with wall is getting added to the "game" commands in main.py as it is a part of the game so to speak

#Taking turns with the ball, reversig axis so that if the right misses the left will get the reset ball coming right at them.