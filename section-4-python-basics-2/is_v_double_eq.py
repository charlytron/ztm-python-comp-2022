###############################################################################
#                         is vs ==                                           #
###############################################################################

# is is a comparison operator that returns True if the two operands are the same object.
# == is an equality operator that returns True if the two operands have the same value.

print(1 is 1) # True
print(1 is not 1) # False
print(1 == 1) # True
print('1' == 1) # False (doesn't get converted to int)
print(1 != 1) # False
print(1 == 2) # False
print(1 != 2) # True
print(1 == True) # True
print(1 == False) # False
print(1 is True) # False
print(1 is False) # False
print(1 is not True) # True
print(1 is not False) # True

print(True == 1) # True because 1 is truthy
print("" == 1) # False because '' is falsy
print([] == 1) # False because [] is falsy
print(10 == 10.0) # True
print([] == []) # True
print([1,2,3] == [1,2,3]) # True

# == checks for value equality

print(True is 1) # False
print("" is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([] is []) # False
print([1,2,3] is [1,2,3]) # False

# is checks if the location in memory is the same
# Things may appear to be the same but they are not the same object in memory
# therefore is will return False

a = [1,2,3]
b = [1,2,3]

a is b # False
a == b # True because the values are the same


# to be continued from 2:39:00 in the video