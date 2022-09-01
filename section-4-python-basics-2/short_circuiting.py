###############################################################################
#                              Short Circuiting                               #
###############################################################################



is_Friend = True
is_User = True

# print(is_Friend and is_User) # True# 

if is_Friend and is_User:
    print("You are allowed to message")

# Short circuiting is a technique that allows us to avoid unnecessary computation
# if a condition is not met.

if is_Friend or is_User:
    print("You are allowed to message")

# Which operation is more efficient?
# The second operation is more efficient because it doesn't need to check if the
# condition is met. If the first condition is already false, the second condition
# is not even evaluated. The interpreter has already done enough work.

# Why is a greater than b
print('a' > 'b') # False
print('a' > 'a') # False
print('a' > 'A') # why True? 
# ascii value of a is 97
# ascii value of A is 65
# The interpreter is comparing the ASCII values of the characters.

print(1 < 2 < 3) # True
print(1 < 2 > 3 < 4) # False, will short circuit
print(1 >= 2 > 3 < 4 > 5) # False, will short circuit
print(1 >= 0) # True
print(0 != 0) # False

# What about the not operator?
print(not(True)) # False
# it's a keyword but also a function
print(not False) # True
print(not 0) # True
print(not 1) # False
print(not -1) # False
print(not(1 == 1)) # False
