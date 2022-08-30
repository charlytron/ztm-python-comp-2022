############################################################
#                 DICTIONARY                               #
############################################################

# Dictionary is a collection of key-value pairs.
# In other languages, a dictionary is a hash table.
# In Python, a dictionary is a dict data type.

dict_1 = {'key_1': 'value_1', 'key_2': 'value_2'}

dict_2 = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
}

# We can access the value of a key in a dictionary by using the key name.

print(dict_1['key_1']) # gives us 'value_1'

# Give it the key and it will give you the value.

print(dict_2['a']) # gives us 1
# print(dict_2['f']) # gives us error

# a dictionary is an unordered collection of key-value pairs.
# The key-value pairs do not exist next to each other in memory.

print(dict_2)

# This prints in order, but if it was a large dictionary it's not guaranteed to be in order.
# The computer has the memory address of each key-value pair, and it can access the value

# Dictionaries and lists are just containers around data.

dictionary = {
  'a': [1,3,4],
  'b': 'HOWL',
  'c': True
}

print(dictionary['a']) # gives us [1,3,4]
print(dictionary['b']) # gives us 'HOWL'
print(dictionary['a'][1]) # gives us 3

my_list = [
  {
  'a': [1,3,4],
  'b': 'HOWL',
  'c': True
},
{
  'a': [4,5,6],
  'b': 'HOWL',
  'c': True
}
]

print(my_list[0]['a']) # gives us [1,3,4]
