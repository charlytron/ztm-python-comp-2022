############################################################
#                     Truthy and Falsy                     #
############################################################

"""
 Until now, we've been using the boolean values True and False
 to represent the truth and falsity of values. But Python has a
 way of converting any value to a boolean value.

 We're converting the type of a value to a boolean value by
 using the built-in function bool().
"""

is_old = bool('Jello')
is_licensed = bool(5)

print(bool('Jello')) # True
print(bool(5)) # True
print(bool(0)) # False
print(bool(None)) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False
print(bool('')) # False

""" 
This is what we call a truthy value.
If we run the bool() function on a value that is not falsy,
we get True.

It's useful for checking the existence of a value.
Username and password are examples of values that are truthy.
"""

if is_old and is_licensed:
    print("You are old enough and licensed to drive")
# elif is_licensed:
    # print("You are licensed to drive")
else:
    print('checkity check check, checkmate')  # outside of the if statement

print('wubba lubba dub dub')  # outside of the if statement


