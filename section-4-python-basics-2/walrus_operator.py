######################################################################
#                          Walrus Operator                           #
######################################################################

# The walrus operator is a new assignment operator in Python 3.8
# It assigns values to variables as part of a larger expression

# The walrus operator is represented by :=

a = "Jello World"

if (len(a) > 10):
    print(f"String is too long: {len(a)} characters.")

if ((n := len(a)) > 10): # Assigns the length of a to n and then checks if n is greater than 10
    print(f"String is too long: {n} characters.") # helps to avoid repeating the same expression

while ((n := len(a)) > 1):
    print(a, n)
    a = a[:-1]
    # a = a[1:] # prints the string in reverse order