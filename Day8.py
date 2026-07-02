
"""
friends = ["John", "Sarah", "Mike", "Emma"]
print (friends)

print(friends[0])
print(friends[2])

print(len(friends))

friends.append("David")
print(friends)

friends.remove("Mike")
print(friends)

print(friends[1])

for friend in friends:
    print(f"{friend} is my friend")


#Now let's combine lists with functions.
# Write a function called greet_friends that takes a list as a parameter
# and prints a greeting for each person in the list.
# Then call it with your friends list.

friends = ["John", "Sarah", "Emma", "David"]

def greet_friends (people):
    for person in people:
        print(f"Greetings {person}, you are my friend")

greet_friends (friends)

"""


#Write a function called add_numbers that:

#Takes a list of numbers as a parameter — call the parameter numbers
#Loops through each number in that list — call the loop variable num
#Prints each number with a message like "The number is 5"
#After the loop finishes, print the sum of all numbers using sum(numbers)

#Then create a list called my_numbers with at least 4 numbers in it, and call the function passing my_numbers in.



numbers = [1,2,3,4,5]

def list_of_numbers (numbers):
    for num in numbers: print(f"The number is {num}")
    print(f"The addition of all the numbers is {sum(numbers)}")

list_of_numbers (numbers)

my_numbers = [10,20,30,40]

list_of_numbers (my_numbers)


