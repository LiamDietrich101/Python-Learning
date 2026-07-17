#nested loops
#continue
print("Nested Loop Example:")
for row in range(1, 4):
    for column in range(1, 4):
        print(f"Row {row}, Column {column}")

"""
Now your turn. Write a nested loop
that produces a multiplication table
for numbers 1 to 3.

Expected output:

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

"""

print("Nested Loop Challenge:")

for number_x in range(1, 4):
    for number_y in range(1,4):
        print(f" {number_x} *  {number_y} = {number_x * number_y}")

