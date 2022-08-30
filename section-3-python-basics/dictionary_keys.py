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

# dictionary = {
#   '123': [1,2,3],
#   '123': 'HOWL', # this will overwrite the previous value
# }

# print(dictionary['123']) # gives us 'HOWL', but why?
# There can only be one key with the same value.
# It represents a bookshelf in that memory location.

# dictionary = {
#   'basket': [1,2,3], # key is 'basket'
#   'Greet': 'HOWL', # this will overwrite the previous value
# }

# print(dictionary['basket']) # gives us [1,2,3]

user = {
  'basket': [1,2,3], # key is 'basket'
  'Greet': 'HOWL', # this will overwrite the previous value
  'age': 25
}

print(user.get('age', 55)) # gives us 55
# grab the age from the user dictionary, 
# if it's not there, give us default value of 55
# If the user already has an age, give us that age.

# A less common way to create dictionaries is to use the dict() function:
user2 = dict(name='SpillyWilly', age=25)
print(user2) # gives us {'name': 'SpillyWilly', 'age': 25}