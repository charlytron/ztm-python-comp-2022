###############################################################################
#                         is vs ==                                           #
###############################################################################

# is is a comparison operator that returns True if the two operands are the same object.
# == is an equality operator that returns True if the two operands have the same value.

print(1 is 1) # True
print(1 is not 1) # False
print(1 == 1) # True
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

# to be continued from 2:39:00 in the video