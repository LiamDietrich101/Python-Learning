def describe_car (brand, colour, doors=4):
    print (f"Brand: {brand}")
    print (f"Colour: {colour}")
    print (f"Doors: {doors}")

describe_car("Toyota", "Red")
describe_car("BMW", "Black", 2)
describe_car(colour="Blue", brand= "Ford", doors=3)

'''
CHALLENGE
Write a function called describe_person with these parameters:

name — required
age — required
country — default value of "Unknown"

Call it three times:

Pass all three arguments in order
Pass only name and age
Use keyword arguments in any order
'''

def describe_person (name, age, country= "Unknown"):
    print (f"Name: {name}, Age: {age}, Country: {country}")

#Defaults must always come last.
# Required parameters first, defaults after.
# Python will throw a SyntaxError otherwise.

describe_person (name= "Liam", age= "37", country= "Northern Ireland")
describe_person ("Genesis", "34")
describe_person ("Ezra", "2", "Northern Ireland")






