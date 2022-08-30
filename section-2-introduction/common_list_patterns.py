###############################################################################
#                      Common List Patterns                                  #
###############################################################################

basket = [1, 8, 3, 9, 5]
# new_basket = basket[:] # creates a new copy of the basket list

# new_basket.sort() # sorts the new copy of the basket list.
basket.sort()
basket.reverse() # reverses the basket in place.
# print(basket) # gives us [5, 9, 3, 8, 1]

# Some tricks with lists that we'll see a lot:

# print(len(basket)) # gives us 5

# list slicing:
# print(basket[1:3]) # gives us [8, 3]
# print(basket[::-1]) # gives us [1, 8, 3, 9, 5]
# not expected, why not?
# print(basket) # gives us [5, 9, 3, 8, 1]

# basket.reverse() is the reversed version, the last action we've taken.
# print(basket[::-1]) we'll see a lot of this for reversing lists
# among other things:

# print(basket[::-1]) # gives us [1, 8, 3, 9, 5]
# print(basket[:])

###############################################################################
#                          RANGE FUNCTION                                    #
###############################################################################

# Great way to quickly create a list of numbers.

# range(start, stop, step)
print(range(1, 100)) # prints range(1, 100)

# Let's wrap this in a list:
# print(list(range(1, 100))) # prints [1, 2, 3, ..., 98, 99]

# We can also write this as:
print(list(range(100))) # prints [0, 1, 2, ..., 99]

###############################################################################
#                               .join()                                      #
###############################################################################

# .join() is a method that joins a list of strings together into a single string.
# It's useful for joining a list of words into a single sentence.

sentence = ' ' 
#sentence.join(['Jello', 'world']) # gives us 'Jello world'
# print(sentence) # gives us ''
# .join creates a new string.

new_sentence = sentence.join(['Jello', 'world']) # gives us 'Jello world'
print(new_sentence) # gives us 'Jello world'

# We can also write it as:
print(' '.join(['Jello', 'world'])) # gives us 'Jello world'

# All we are doing is combining lists into a single string.

###############################################################################

