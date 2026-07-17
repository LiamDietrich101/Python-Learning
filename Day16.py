#pass
print("CONTINUE Example:")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

#continue
print("PASS Example:")

for number in range(1, 6):
    if number == 3:
        pass
    print(number)

#CHALLENGE
#Loop from 1 to 10, print only the odd numbers
# using continue to skip the even ones.
# Hint — a number is even when number % 2 == 0.

#challenge
print("Challenge Example:")

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)


