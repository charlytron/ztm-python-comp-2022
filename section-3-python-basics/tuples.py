###############################################################################
#                                   TUPLES                                    #
###############################################################################

# Tuples are immutable 'lists'.
my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'a' # gives us TypeError: 'tuple' object does not support item assignment
print(my_tuple[1]) # gives us 2
print(5 in my_tuple) # gives us True

# Tuples are useful for storing data that won't change.
# Tuples are faster than lists and they tell other programmers that the data is immutable.
# They make your code safer, more predictable because you can't accidentally change the data.

# Con is that tuples are less flexible than lists.
# We can't add or remove items from a tuple.
# We can't change the order of items in a tuple.

# Tuples by their nature are more performant than lists.
# example: use of geolocation data (latitude and longitude)

user = {
 'basket': [1,2,3],
 'Greet': 'HOWL',
 }

print(user.items()) # gives us dict_items([('basket', [1,2,3]), ('Greet', 'HOWL')])
# in other words, a series of comma-separated tuples.

# A tuple is a completely valid key in a dictionary.

user2 = {
 (1,2): [1,2,3],
 'Greet': 'HOWL',
 }

# We access the tuple thusly:
print(user2[(1,2)]) # gives us [1,2,3]












# user = {
#  'basket': [1,2,3],
#  'Greet': 'HOWL',
#  }

