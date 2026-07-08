# Today it's all about functions.
# The idea is to do several programming challenges to consolidate the logic of how functions work
# and to be able to write them naturally.
#from variables import name

'''
#CHALLENGE 1
#Write a function called greet_user that takes a name and a time_of_day as parameters
# and returns a greeting like "Good morning, Liam!" or "Good evening, Liam!" depending on what's passed in.
# Call it a few times with different names and times of day.


name = input("What is your name? ")
time_of_day = int(input("What time is it? "))

def greet_user(first_name,time_of_the_day):
    if time_of_the_day < 12:
        return(f"Hello {first_name} good morning!")
    elif time_of_the_day <=17:
        return(f"Hello {first_name} good afternoon!")
    else:
        return (f"Hello {first_name} good evening!")

print(greet_user(name, time_of_day))


#CHALLENGE 2
# Write a function called calculate_discount that takes a price and a discount_percentage as parameters
# and returns the final price after the discount is applied. For example, a price of 100 with a 20% discount should return 80.
# Call it with a few different prices and discounts and print the results.


def calculate_discount(price_of_item, percentage_of_discount):
    return round(price_of_item - (price_of_item * percentage_of_discount / 100), 2)

try:
    price = int(input("What is the price of the product? "))
    discount_percentage = int(input("What is the discount percentage? "))
    print(f"The final price is £{calculate_discount(price, discount_percentage)}")

except ValueError:
    print("That wasn't a valid number!")
'''

#Challenge 3 — Password Checker
# Write a function called password_checker that takes a password as a parameter,
# call it user_input inside the function to keep the boundary clear, and returns:
# "Too short" if the password is less than 8 characters
# "Weak" if it's 8 characters or more but contains no numbers
# "Strong" if it's 8 characters or more and contains at least one number
# Then ask the user to enter a password outside the function, store it in a variable called password,
# and call the function passing password in. Print the result.
# Hint — to check if a string contains any numbers use this: any(char.isdigit() for char in user_input),
# this returns True if any character is a digit.


def password_checker(user_input):
    if len (user_input) < 8:
        return ("The password is too short")
    elif not any(char.isdigit() for char in user_input):
        return "The password is weak"
    else:
        return "The password is strong"

password = input("What is the password? ")

print(password_checker(password))




















