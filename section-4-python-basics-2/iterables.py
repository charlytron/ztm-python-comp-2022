##############################################################################
#                                    Iterables                              #
##############################################################################

# Iterables are objects or collections that can return one of their elements at a time, such as
# a list, a string, dictionary, tuple, set.
# 
# You can loop over an iterable with a for loop.

user = {
    'name': 'Growlem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
        print(item) # prints each item in the dictionary

for item in user.values():
        print(item) # prints each value in the dictionary

for item in user.keys():
        print(item) # prints each key in the dictionary

for key, value in user.items():
        print(key, value) # prints each key and value in the dictionary, 
        # unpacking the tuple. It's a common pattern to use key, value.

# for item in 67:
    # print(item) # TypeError: 'int' object is not iterable
    # 67 is not an iterable, not a collection of items.

