#Day 21

#Learning about Inheritence, slicing and finish the game!

# Day 21:
# 4) Detect collision with food
# 5) Create a scoreboard
# 6) detect collison with wall 
# 7) detect collision with tail



#Class Inheritence

#code up a chef, bake() stir() measure()
#hire a 2nd chef and take some of the things it knows to add them to your next chef as well as its own skills(),, this is class inherited

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)



#detect collision with food 
#created food.py which would be its own class, render itself as a small circle on the screen and when its hit move randomly around the screen



#creating a scoreboard 
#keep track of how many peices of food have been eaten, scoreboard will be a 'turtle' so going to make this a seperatepy again and import it into the main game.



#Detecting collision with wall (and also tail)
#creating boundry box around the outside for the wall,, will add this to the py-thon game... probably should start calling things main.py etc like a professional, also because its like the standard etc etc.
#adding game over to scoreboard as that is doing most of the writing side of things.
#Tails wise we need to add segments to the snake to make it longer then we can detect collision with the tail.
#adding segments to the snake.py.
#more collision with on py-thon but this time its the tail.




#Learning about slicing 
#piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
#           = ["0", "1", "2", "3", "4", "5", "6", "7"]
#piano_keys[2:5]    --- this is the slice example

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])