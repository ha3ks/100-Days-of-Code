#Day 4

#Randomisation and Python Lists

import random
random_integer = random.randint(1, 10)
print(random_integer)

randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


#EXERCISE Random Exercise
import random
randomCoin = random.randint(0, 1)
if randomCoin == '0':
    print("Heads")
else:
    print("Tails")


#Lists
#example structure    fruits = ["Cherry", "apple", "pear"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

states_of_america.append("Angelaland") #adds one item
states_of_america.extend(["Angelaland", "Jack Bauer Land"])


#EXERCISE Banker Roulette - who will pay the bill?
import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")


#Working with Nested Lists
print(states_of_america[50]) #will give an error as it is out of range.
num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1]) #-1 as it will turn 1 to 0 and not give an off by 1 error

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries","Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale","Tomatoes", "Celery", "Potatoes"]

dirty_dozen = ["fruits, vegetables"]
print(dirty_dozen)
#prints with multiple brackets to show its using lists upon lists


#EXERCISE Treasure Map - but better
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

