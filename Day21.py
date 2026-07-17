#Octal and Hexadecimal

print(0b1010)
print(0o17)
print(0xFF)


"""
0b prefix means binary
0o prefix means octal
0x prefix means hexadecimal
"""

print(3e4)    # 3 × 10⁴ = 30000
print(2.5e-3) # 2.5 × 10⁻³ = 0.0025


try:
    print(1/0)
except ArithmeticError:
    print("maths error caught")


try:
    my_list = [1, 2, 3]
    print(my_list[10])
except LookupError:
    print("lookup error caught")



def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("caught outside the function")