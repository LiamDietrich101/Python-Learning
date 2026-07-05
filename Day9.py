"""

#tuples
coordinates = (51.5074, -0.1278)
print(coordinates)
print(coordinates[0])
print(coordinates[1])
coordinates[0] = 99.9999



#dictionaries

person = {
    "name": "Liam",
    "age": 28,
    "city": "Belfast",
    "job": "AI & Data Consultant"
}

print (person)

print(person["name"])
print(person["age"])

person["email"] = "liam@email.com"
print(person)

person["age"] = 29
print(person["age"])

print(person)

for key in person:
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")


print(person.keys())
print(person.values())

"""

#Challenge
#Write a program that:
# 1) Creates a dictionary called student with these keys: name, grade, score
# 2) Prints a personalized message using f-strings showing all three values
# 3) Then asks the user if they want to update the score — if yes, ask for the new score and update the dictionary
# 4) Print the updated dictionary at the end
#You'll need input, if/else, and dictionary updating. Have a go.



student = {
    "name": "Liam",
    "grade": "A",
    "score": "10",
}

for key, value in student.items():
    print(f"{key}: {value}")

score_question = input("Do you want to update your score?")

if score_question == "yes":
    student["score"] = int(input("What is the new score?"))
else:
    print ("Score not updated")

print(student)










