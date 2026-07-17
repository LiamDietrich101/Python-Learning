#del and not in


fruits = ["apple", "banana", "cherry", "mango"]

print(fruits)

del fruits[1]

print(fruits)

if "banana" not in fruits:
    print("banana is gone")

'''
CHALLENGE
Create a list of 5 cities
Delete the third one using del
Print the list
Check if a city that you deleted is not in the list 
and print a message confirming it's gone
'''
print("Challenge Example:")

cities = ["Belfast", "Bangor", "Portadown", "Portrush", "Lisburn"]

print (cities)

del cities[2]

print (cities)

if "Portadown" not in cities:
    print("Portadown is gone")

cities.insert(1, "London")

print (cities)



