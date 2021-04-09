#Day 16

#Today were talking about OOP, Object Oriented Proramming hereto referred to as OOP-d'ere-it-is.

#previously was coding as 'procedural programming', does one thing, then another then another.

#OOP means we can split a larger task into smaller peices and some of those peices can be reused.

#an object is made from atributes and methods, what it has and what it does.

#Classes 

#object    class
#car = CarBluePrint()

#looking into TurtleGraphics.

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
#### <turtle.Turtle object at 0x0000026912B1CF70>
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100) #ITS ALIVE!!! it moved!!!

my_screen = Screen()
print(my_screen.canvheight)
#### <turtle.Turtle object at 0x000001624367CF70>
#### 300
my_screen.exitonclick()
#will allow it to run till we click on it.


#Practice modifying object atributes and calling methods.

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squitle', 'Charmander'])
table.add_column("Pokemon Type", ['Electric', 'Water', 'Fire'])
table.align = "L" #Aligning with left hand side.
print(table)


