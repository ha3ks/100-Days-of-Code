# Day 2

# Data Types - Strings, Integar, Float & Boolean

#String 
 
print("Hello"[4])

#Still treats numbers as text as itsin quotations
print("123" + "345")
#displays 123456

#Integar

print(123 + 345)

#Large numbers have commas and in python these can be replaced by underscores (benefit is human reading)
123_456_789

#Float
#when you have acutal decimal places, this can move around the number (floating point number)
3.14259

#Boolean
#can be one of two things

True
False

#Data Types Exercise
#Add two numbers together and print output

#Don't change the code below
two_digit_number = input("Type a two digit number: ")
#Don't change the code above
####################################
#Write your code below this line 
#Check the data type of two_digit_number
print(type(two_digit_number))
#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
#Add the two digits togeter
two_digit_number = first_digit + second_digit
print(two_digit_number)

#maths
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3 #raise to power

# PEMDAS
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

print(3 * 3 + 3 / 3 - 3)
#prints 7

#to print 3 we need to add some parenthases
print(3 * (3 + 3) / 3 - 3)


#EXERCISE BMI Calculator
#Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Don't change the code above
#Write your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)


#rounding
print(round(8 /3,2))
#outputs 2.67 as its specified 2 decimal places

#floor division
print(8 // 3)
#outputs 2 without converting to Integar

result = 4 / 2
result /= 2
print(result) # = 1 its 4 divide 2 then divide again

#f strings
score = 0
height = 1.8
isWinning = True
print("your score is " + str(score))
#f string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#EXERCISE Life in Weeks
age = input("What is your current age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days remaining, {weeks_remaining} weeks remaining and {months_remaining} months remaining. Spend them wisely learning Python the greatest most most most most most most Kanye spending millions on a hologram of a dead guy only to toot his own horn, programming language ever.")