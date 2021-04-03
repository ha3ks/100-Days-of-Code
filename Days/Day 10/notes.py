#Day 10

#making a calculator today

#Functions and outputs
# def my_function():
#     result = 3 * 2
#     return result

# output = my_function() #can pass output to other things like print

# print(output)

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #print(f"{formatted_f_name} {formatted_l_name}")
    return(f"{formatted_f_name} {formatted_l_name}")

formatted_string = format_name("daN", "MURRAY")
#print(formatted_string)
print(format_name("daN", "MURRAY"))



#multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return (f"Result: {formatted_f_name} {formatted_l_name}")

print(format_name(input("What is your first name? "), input("What is your last name? ")))



#EXERCISE Days in Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#Tests
import unittest

class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(days_in_month(2018, 2), 28)

    def test_2(self):
        self.assertEqual(days_in_month(2020, 2), 29)

    def test_3(self):
        self.assertEqual(days_in_month(2019, 4), 30)

    def test_4(self):
        self.assertEqual(days_in_month(1045, 5), 31)

print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)



#Docstrings
#example
def format_name(f_name, l_name):
#---> this is the docstring, the first line after a declaration, needs to have 3 quotation marks : """Information goes here"""
    if f_name == "" or l_name == "":
        return "You didn't provide any inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return (f"Result: {formatted_f_name} {formatted_l_name}")



#Calculator Part 1 - Combining Dictionaries and Functions
#Adding
def add(n1, n2):
  return n1 + n2
#Subtraction
def subtract(n1, n2):
  return n1 - n2
#Multiplication
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What is the first numeber?: "))
### num1 = float(input("What is the first numeber?: "))
num2 = int(input("What is the second numeber?: "))
    
for symbol in operations:
        print(symbol)
operation_symbol = input("Pick and operation from the line above: ")
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What is the next numeber?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


#While Loops, Flags and Recursion
if input("Type 'y' to continue calculating with {answer}:") == "y":
    num1 = answer

#I really do take bad notes sometimes.

#Calculator Finishing touchees and bug fixes 
#int gets changed to float so that things like 4.5 can be used as numbers now.