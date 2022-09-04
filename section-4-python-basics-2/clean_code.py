###############################################################################
#                           Clean Code - Python Basics 2                      #
###############################################################################

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4)) # even

# Another way to write the above function:

def is_even(number):
    if number % 2 == 0:
        return True
    return False

# How can we make this function better?

def is_even(number):
    return number % 2 == 0
    # We don't need the if statement because the return statement will return
    # True or False depending on the condition
print(is_even(5)) # False