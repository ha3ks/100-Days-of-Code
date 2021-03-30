#Day 6

#Functions
# print("Hello")
# num_char = len("Hello")
# print(num_char)

#defining custom function
def my_function():
    print("Hello")
    print("bye")

#calling Functions
my_function()


##Using Reeborgs world to understand multiple functions (moving a robot in a grid) 

# individual commands
# move()
# move()
# turn_left()
# turn_left()
# move()
# move()
# turn_left()
# turn_left()

# however we can put these into a function so we wont have to write them out manually each time we

# def turn_around():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# move()
# move()
# turn_around()
# move()
# move()
# turn_right()


# Make a square example
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()


#EXERCISE Hurdles loop
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():    
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(6):
#     hurdle()


#Indentation
#def my_function():
#****print("Hello")
#****print("World")

#Kinda like a file structure

#This is a test in VIM

#Python documentation states to use Spaces instead of Tabs... crap!


#While loops

# for item in list_of_items:
#     #Do something to each item

# for number in range(a, b):
#     print(number)

#Using a while loop on the hurdles exercise
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():    
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     hurdle()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)


#EXERCISE More Hurdles 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():    
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         hurdle()
#     else:
#         move()


#EXERCISE Final Hurdle
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():    
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         hurdle()
#     else:
#         move()