#Day 5

#loops
#for item in list_of_items:
    #do something

fruits = ["Apple", "Orange", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    #will keep looping        print(fruits) 
print(fruits) #if its outside the indent it will run once as its not part of the for loop


#EXERCISE Average Height
student_heights = input("Input a list of student heights in cm ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)


#EXERCISE High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")


#for loops and the range() function
# for number in range (a,b):
#    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)


#EXERCISE Adding even numbers
total = 0
for number in range(2, 101, 2):
    total += number
    print(number)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)


#EXERCISE The Fizz Buzz Interview
# print each number from 1 to 100
# when the number is divisible by 3 then print Fizz
# when the number is divisible by 5 print Buzz
# and if number is divisible by 3 and by 5 then print FizzBuzz

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz") #as if else stops at first correct i.e. 15 is divisible by 3 but also 5 so this line of code moves to the top and is run first to catch these then rest of examples can rub below including the print number for the numbers in the list not just Fizz Buzz
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
