############################################################
#                  Dictionary Methods                      #
############################################################

# dictionary = {
#  'basket': [1,2,3],
#  'Greet': 'HOWL',
#  }

# print(dictionary.keys()) # gives us dict_keys(['basket', 'Greet'])
# print(dictionary.values()) # gives us dict_values([[1,2,3], 'HOWL'])
# print(dictionary['basket']) # gives us [1,2,3]

user = {
 'basket': [1,2,3],
 'Greet': 'HOWL',
 }


# print(user['age']) # gives us error. KeyError: 'age'
print(user.get('age')) # gives us None

print(user.get('age', 55)) # gives us 55, adding a default value.
## Grab the age from the user dictionary,
## if it's not there, give us default value of 55

# If the user already has an age, give us that age.
user2 = {
 'basket': [1,2,3],
 'Greet': 'HOWL',
 'age': 25
 }

print(user2.get('age', 55)) # gives us 25

# Another less common way to create dictionaries is to use the dict() function:

user3 = dict(name='SpillyWilly', age=25)
