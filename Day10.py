"""

try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except:
    print("That wasn't a valid number!")



try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except ValueError:
    print("That wasn't a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")



try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except ValueError:
    print("That wasn't a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Program completed.")

"""

#Now let's do a practical challenge that combines exception handling with what you've learned before. Write a program that:

#Asks the user to enter two numbers
#Divides the first by the second
#Handles a ValueError if either input isn't a number
#Handles a ZeroDivisionError if the second number is zero
#Uses finally to print "Calculation complete." at the end

try:
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    division_result = number_1 / number_2
    print(f"The result of {number_1} divided by {number_2} is {division_result}")
except ValueError:
    print("That wasn't a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Calculation completed.")











