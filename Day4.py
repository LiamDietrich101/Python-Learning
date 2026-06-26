
"""
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
elif age < 13:
    print("You are an child.")
else:
    print("You are a teenager.")
#Your version works perfectly — both approaches are correct.
#But as your programs get more complex, writing conditions in a logical order
#makes your code easier to read and debug.
#This is called code readability
#and it's something professional developers think about constantly.

"""

"""
# this is another option with ascending age logic & it's better

age = int(input("How old are you? "))
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
    
"""
"""
password = str(input("Please enter your password: "))
if password == "1234":
    print("Password is valid")
else:
    print("Password is not valid")

"""

""" 

Let's do one final challenge for today that combines everything 
— control flow, user input, type conversion and f-strings together.

Write a program that:

Asks the user for their name and their salary
If salary is above 50000 — print "{name}, you are a high earner."
If salary is between 25000 and 50000 — print "{name}, you are an average earner."
If salary is below 25000 — print "{name}, you are a low earner."

"""
#ask name
name = input("What is your name? ")

#ask salary
salary = input("Please enter your salary: ")


salary = int(salary)
if salary < 25000:
    print(f"{name.title()} you are a low earner.")
elif salary < 50000:
    print (f"{name.title()} you are a average earner.")
else:
    print(f"{name.title()} you are a high earner.")





