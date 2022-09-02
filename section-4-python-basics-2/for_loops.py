##############################################################################
#                                  FOR LOOPS                                 #
##############################################################################

# For loops are used to iterate over a sequence (that is either a list, a tuple,
# a dictionary, a set, or a string).

for item in 'Python':
    print(item) # prints each letter in the string 'Python', known as an iterable

# item is a variable that is created when the for loop is executed. It is arbitrary
# and can be named anything. It is used to represent each item in the sequence.

for item in ['Moishe', 'Juan', 'Zarah']:
    print(item) # prints each item in the list

# Can we do the same with a set?
for item in {'Moishe', 'Juan', 'Zarah'}:
    print(item) # prints each item in the set

# Can we do the same with a tuple? Yip!
for item in ('Moishe', 'Juan', 'Zarah'):
    print(item) # prints each item in the tuple

# Can we do the same with a dictionary? 
# You bet, but it will only print the keys.
for item in {'name': 'Moishe', 'age': 32}:
    print(item) # prints each key in the dictionary

##############################################################################
#                                 Nested loops                               #
##############################################################################

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)
# prints each item in the tuple and each item in the list