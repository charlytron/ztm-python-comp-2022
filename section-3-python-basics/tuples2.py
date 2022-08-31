###############################################################################
#                                 Tuples2                                     #
###############################################################################

# Tuples are immutable lists.

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2] # gives us (2,) 
print(new_tuple) # gives us (2,) but why?

new_tuple2 = my_tuple[1:4] # gives us (2,3,4)
print(new_tuple2) # gives us (2,3,4)

x,y,z, *other = (1,2,3,4,5) # gives us (1,2,3,4,5)
print(other) # gives us (4,5)

# Tuple has only two methods that we care about:
# .count() and .index()

print(my_tuple.count(3)) # gives us 1 instance of 3 in the tuple
print(my_tuple.index(3)) # gives us 2, the index of the first instance of 3 in the tuple
print(len(my_tuple)) # gives us 5, the length of the tuple