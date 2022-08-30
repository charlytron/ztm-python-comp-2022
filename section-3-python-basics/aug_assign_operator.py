############################################################
#             Augmented assignment operator                #
############################################################

some_value = 5
some_value = some_value + 2

print(some_value) # 7

#  There's a better way to do this:

some_value += 2 # same as some_value = some_value + 2
some_value -= 2 # same as some_value = some_value - 2

# In order to use the augmented assignment operator, you need 
# to make sure that the variable is mutable and has some previous value.

some_value *= 2 # 10

