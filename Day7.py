# today we will learn about functions

"""

# 1st example
def greet():
    print("Hello, welcome to Python!")
greet ()


# 2nd example with parameters
def greet(name):
    print(f"Hello {name}, welcome to Python!")
greet("Liam")
greet("John")


# 3rd example with return value
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print (result)



# Write a function called calculate_bmi that takes two parameters
# — weight in kilograms and height in metres —
# and returns the BMI calculated as weight / (height * height).


def calculate_bmi(height, weight):
    return round(weight / (height * height), 2)
height = float (input ("what is your height?"))
weight = float ( input ("what is your weight?"))
result = calculate_bmi (height, weight)
print (f"Your BMI is {result}")

"""

def grade_checker (a):
    if a >= 90:
        return ("Your grade is A")
    elif a>= 80:
        return ("Your grade is B")
    elif a>= 70:
        return ("Your grade is C")
    elif a>= 60:
        return ("Your grade is D")
    else:
        return ("Your grade is F")

a = int (input ("what is your grade?"))

result = grade_checker(a)
print (result)










