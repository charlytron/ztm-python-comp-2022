###############################################################################
#                           Dictionary Methods                                #
###############################################################################


#################################
#                               #
# .keys(), .values(), .items()  #
#                               #
#################################

user = {
 'basket': [1,2,3],
 'Greet': 'HOWL',
  'age': 25
 }

print('basket' in user) # gives us True
print('age' in user) # gives us True
print('name' in user) # gives us False

# Dictionary methods are useful for manipulating dictionaries.
# We can use the keys() method to check the keys in a dictionary:

print('size' in user.keys()) # gives us False
print('age' in user.keys()) # gives us True

# If we want to check values, we can use the values() method:

print([1,2,3] in user.values()) # gives us True
print('HOWL' in user.values()) # gives us True')

# If we want to check both keys and values, we can use the items() method:

print(user.items()) # gives us dict_items([('basket', [1,2,3]), ('Greet', 'HOWL'), ('age', 25)])

# ('age', 25) is actually a tuple.

###############################################################################
#                                                                             #
#         clear(), copy(), pop(), popItem(), update()                         #
#                                                                             #
###############################################################################

# print(user.clear()) # gives us None, removing all keys and values from the dictionary.
# print(user) # gives us {}

# print(user.copy()) # gives us {'basket': [1,2,3], 'Greet': 'HOWL', 'age': 25}

# user2 = user.copy()
# print(user)
# print(user2)

# But if we clear the first user, the second user will still have the same values.

# print(user.clear()) # gives us None, removing all keys and values from the dictionary.
# print(user2) # gives us {'basket': [1,2,3], 'Greet': 'HOWL', 'age': 25}

# print(user.pop('age')) # gives us 25, returning the value of what got removed.
# print(user) # gives us {'basket': [1,2,3], 'Greet': 'HOWL'}

# print(user.popitem()) # gives us ('age', 25), returning the key and value of what got removed.
# Doesn't always return the last item in the dictionary. Be careful!

print(user.update({'age': 85})) # gives us None, updating the dictionary with a new key and value.
print(user) # gives us {'basket': [1,2,3], 'Greet': 'HOWL', 'age': 85}
