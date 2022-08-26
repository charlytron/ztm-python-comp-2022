# int and float

# print(type(3 + 5)) # <class 'int'>
# print(type(3 * 5)) # <class 'int'>
# print(type(8 - 5)) # <class 'int'>
# print(type(8 / 5)) # <class 'float'>

# Float takes up more space than int
# Int is stored in memory as binary
# Float stores number in two different locations in memory

print(type(10.56)) # <class 'float'>

# We need more memory to store a float

print(type(20+1.1)) # <class 'float'>
print(type(9.9+1.1)) # still a float because 11.0 is stored in memory as a float

# We can convert int to float

print(2 ** 3) # 8
print(2 // 4) # 0 (integer division) gets rounded down

# modulo operator: remainder of division
print(10 % 3) # 1