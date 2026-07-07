
"""

CHALLENGE 0
num1 = 1
num2 = 2

def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(num1, num2)
print (result)


CHALLENGE 1
Write a function called calculate_area that takes width and height as parameters
and returns the area (width multiplied by height). 
Call it with any two numbers and print the result.

width = 10
height = 50
def calculate_area(width, height):
    return width * height
result = calculate_area(width, height)
print (result)


CHALLENGE 2
Write a function called is_even that takes a single number as a parameter and returns True if the number is even
and False if it's odd. Then call it with a few different numbers and print the results.
Hint — to check if a number is even you use the modulo operator % which gives you the remainder of a division.
So 10 % 2 gives 0 because 10 divides evenly by 2, and 7 % 2 gives 1 because there's a remainder.

"""

number= int (input("Enter a number: "))
def is_even (value):
    return value % 2 == 0
print (is_even(number))



