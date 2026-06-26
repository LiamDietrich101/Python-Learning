
#ask for the name
name = input("What is your name? ")

#ask their age
age = input("How old are you? ")

#ask city
city = input("Where are you from? ")

print("Hi, my name is " + name + ", I am " + age + " and I live in " + city)

print(type(age))

age = int(age)

print(age + 10)

#Now here's a challenge that combines everything from today. Write a program that:

#Asks the user for their name
#Asks for their birth year
#Calculates how old they are by subtracting their birth year from 2026
#Prints a sentence like: Liam, you are 28 years old.



#ask for the name
name = input("What is your name? ")

#ask their age
birth_year = input("What year were you born? ")

#convert string to int
birth_year = int(birth_year)

age = 2026 - birth_year

#print (name + " you are " + str(age) + " years old")


#print(f"{name} you are {age} years old")

print(f"{name.title()} you are {age} years old")

