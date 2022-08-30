############################################################
#                       LIST SLICING                       #
############################################################

# List slicing is a way to access a subset of a list. A bit like string slicing.

import string


string = 'abcdefghijklmnopqrstuvwxyz'
print(string[0:3:1]) # abc [start:end:step]

amazon_cart = [
  'milk',
   'bread',
   'eggs',
   'apples',
   'bananas'
]

print(amazon_cart[0:3:1]) # milk, bread, eggs
print(amazon_cart[0::2]) # milk, eggs go all the way to the end of the list, every other item
print(amazon_cart[::-1]) # backwards
print(amazon_cart[::-2]) # backwards, every other item

# Remember how strings are immutable?

# greet = 'Jello World'
# greet[0] = 'H' # This will throw an error.

# The interesting thing is that lists are mutable.

amazon_cart[0] = 'hot_tamales' # This will change the first item in the list.
print(amazon_cart) # ['hot_tamales', 'bread', 'eggs', 'apples', 'bananas']
print(amazon_cart[1:3]) # ['bread', 'eggs']
print(amazon_cart) # ['hot_tamales', 'bread', 'eggs', 'apples', 'bananas'])

# The list did not change. With list slicing, we're creating a new list.

new_cart = amazon_cart[1:3] # ['bread', 'eggs']

new_cart = amazon_cart # assigns new_cart to amazon_cart's position in memory.
new_cart[0] = 'tamales' # This will change the second item in the list.
print(new_cart) # ['hot_tamales', 'bread', 'eggs', 'apples', 'bananas']

# If we want to copy a list, we can use:

new_cart = amazon_cart[:] # This will copy the list, using the slice syntax.
