#Day 9

#The Python Dictionary: Deep Dive
#   {key, value}
#   example
#   {"Bug", "An error in a program that prevents the program from running as expected."}

#if you wanted more in the dictionary you would end seperate entries with a comma and add in : between item entries
#   {
#   "Bug:": "An error in a program that prevents the program from running as expected.",
#   "Function": "A peice of code that you can easily call over and over again.",
#   "Loop": "The action of doing something over and over again.",
#   }

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    #"Loop": "The action of doing something over and over again.",
}

#print(programming_dictionary["Bug"])

#adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

#Create and empty Dictionary
#   empty_dictionary= {}

#wipe an existing dictionary
#   programming_dictionary = {}
#   print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



#EXERCISE Grading Program
#Works in main 100daysofcode dir but noted here as main.py
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Create an empty dictionary called student_grades.
student_grades = {}

#Write your code below to covert scores into grades.
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

with open('testing_copy_2.py', 'w') as file:
  file.write('student_scores = {"Harry": 41, "Ron": 91, "Hermione": 89, "Draco": 69,"Neville": 71}\n\n')
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[8:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import testing_copy_2

import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def test_1(self): 
    with patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      expected_print = "{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_2(self): 
    with patch('sys.stdout', new = StringIO()) as fake_out:
      testing_copy_2.test_func()
      expected_print = "{'Harry': 'Fail', 'Ron': 'Outstanding', 'Hermione': 'Exceeds Expectations', 'Draco': 'Fail', 'Neville': 'Acceptable'}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

print('\n\n\n.\n.\n.')
print('Checking if what you printed matches the target output for two different dictionaries...')
print('Running some tests on your code:')
print('.\n.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
os.remove('testing_copy_2.py') 



#Nesting lists and Dictionaries
#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]


#EXERCISE Dictionary in List



#Secret_Auction Instructions

