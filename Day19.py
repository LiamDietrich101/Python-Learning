list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(f"list_a: {list_a}")
print(f"list_b: {list_b}")

list_c = [1, 2, 3]
list_d = list_c[:]
list_d.append(4)
print(f"list_c: {list_c}")
print(f"list_d: {list_d}")

"""

ways to clone a list:
list_b = list_a[:]
list_b = list(list_a)
list_b = list_a.copy()

"""

"""
CHALLENGE:
Create a list of 3 numbers
Create an alias of it and 
append a number — show both lists changed
Create a proper clone using [:] 
and append a number — show only the clone changed

"""
print ("")
print ("")
print ("CHALLENGE example:")

numbers_1 = [1, 2, 3]
numbers_2 = numbers_1
numbers_2.append(40)
print(f"numbers_1: {numbers_1}")

numbers_3 = numbers_1 [:]
print (f"numbers_3: {numbers_3}")

numbers_3.append(500)
print (f"new numbers_3: {numbers_3}")

