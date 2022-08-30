############################################################
#                        DICTIONARY KEYS                   #
############################################################

# a dictionary can hold any type of data, including other dictionaries.
# But what about the keys?

# dictionary = {
#   123: [1,2,3],
#   True: 'HOWL',
#   [100]: True
# }
 
# print(dictionary[123]) # gives us [1,2,3]
# print(dictionary[True]) # gives us 'HOWL'
# print(dictionary[[100]]) # gives us error. Unhashable type: 'list'

# Dictionary keys need to have a special property called hashable.
# A key needs to be immutable and hashable to be able to be used as a key in a dictionary.

# Dictionary doesn't want to lose the value of a key if you change the key.

# That said, we can use tuples as keys.

# 99% of the time, a key is usually a string, something descriptive like 'name', 'age', 'height', etc.

dictionary = {
  '123': [1,2,3],
  '123': 'HOWL', # this will overwrite the previous value
}

print(dictionary['123']) # gives us 'HOWL', but why?
# There can only be one key with the same value.
# It represents a bookshelf in that memory location.


