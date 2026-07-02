#example
'''
count = 0
while count < 5:
    print(count)
    count = count + 1
'''

'''
password = input("Please type the password ")
while password != "python123":
    correct_password_message = input("Please type the password ")
print ('That is correct')

'''

while True:
    password = input("Please type the password ")
    if password == "python123":
        break
print("That is correct")

