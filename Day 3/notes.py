#Day 3

#Conditional Statements such as if/else

# if condition:
#     do this 
# else:
#     do this

print("Welcome to the Rollercoaster!")
height = (input("What is your height in cm? "))

if int(height) >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to get taller to ride, looser.")


#EXERCISE Odd or Even
number = (input("Which number do you want to check? "))
if int(number) % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")


#Nested if/else
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

print("Welcome to the Rollercoaster!")
height = (input("What is your height in cm? "))

if int(height) >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay £5")
    elif age <= 18: #can use elif to add many more conditions
        print("Please pay £7")
    else:
        print("Please pay £15 buck little man, put that shit in my hand!")
else:
    print("Sorry, you have to get taller to ride, looser.")


#EXERCISE BMI 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


#EXERCISE Leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


#Multiple if statements in succession
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

#We want to charge folks an extra £3 if they want a photo of them hiding behind the seat on the rollercoaster, space mountain was scary and that drop came out of nowhere!

print("Welcome to the Rollercoaster!")
height = (input("What is your height in cm? "))
bill = 0
if int(height) >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are £5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7")
    else:
        bill = 15
        print("Adult tickets are £15 buck little man, put that shit in my hand!")
    
    wants_photo = input("Do you want a photo taken? type Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill £{bill}")

else:
    print("Sorry, you have to get taller to ride, looser.")


#EXERCISE Pizza Order Practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")


#Logical Operators
# if condition1 & condition2 & condition3:
#     do this
# else:
#     do this

print("Welcome to the Rollercoaster!")
height = (input("What is your height in cm? "))
bill = 0
if int(height) >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are £5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7")
    ## Adding in the code here as another elif
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
else:
    bill = 15
    print("Adult tickets are £15 buck little man, put that shit in my hand!")
    
    wants_photo = input("Do you want a photo taken? type Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill £{bill}")
    else:
        print("Sorry, you have to get taller to ride, looser.")


#EXERCISE Love Calculator 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")