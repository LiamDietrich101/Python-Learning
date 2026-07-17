name = "Liam"

def greet(username):
    name = "stranger"
    print(f"Inside function: {name}")

greet("Genesis")
print(f"Outside function: {name}")


print ("")
print ("Next\nExample:")
print ("")


name = "Liam"

def greet(username):
    print(f"Inside function: {username}")

greet("Genesis")
print(f"Outside function: {name}")


'''
CHALLENGE

Now your turn. Write a function called set_city that:

Has a parameter called location
Inside the function, create a variable called city and set it to "Belfast"
Print the inside city

Before the function, create a global variable also called city and set it to "London".
After calling the function, print the global city.
'''


print ("")
print ("DAY CHALLENGE:")
print ("")



city = "London"

def set_city (location):
    city = "Belfast"
    print (f"Inside function: {city}")

set_city ("banana")
#named it banan to showcase the parameter is not being used

print (f"Outside the function: {city}")