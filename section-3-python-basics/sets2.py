###############################################################################
#                                     SETS                                    #
###############################################################################

# Sets are unordered collections of unique elements.
# Know what tools you need to use.

"""
# sets methods
 .add()
 .clear()
 .copy()
 .difference()
 .difference_update()
 .discard()
 .intersection()
 .intersection_update()
 .isdisjoint()
 .issubset()
 .issuperset()
 .pop()
 .remove()
 .symmetric_difference()
 .symmetric_difference_update()
 .union()
 .update()
"""
my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}

"""
print(my_set.difference(your_set)) # gives us {1,2,3}
print(my_set.discard(5)) # gives us None, removes the element 5 from the set.
print(my_set) # Not modified.
print(my_set.difference_update(your_set)) # gives us None, removes the elements in the set.
print(my_set) # gives us {1,2,3}, removing the difference between the sets.
"""
# .intersection()
# print(my_set.intersection(your_set)) # gives us {4,5}, the common elements between the sets.

print(my_set.isdisjoint(your_set)) # gives us False, because there's common elements between the sets.

print(my_set.union(your_set)) # gives us {1,2,3,4,5,6,7,8,9,10},
# returning a new set with all the elements in the sets.

print(my_set | your_set) # gives us {1,2,3,4,5,6,7,8,9,10},

print(my_set.intersection(your_set)) # gives us {4,5}, the common elements between the sets.

print(my_set & your_set) # gives us {4,5}, the common elements between the sets.

print(my_set.issubset(your_set)) # gives us False, 
# because my_set is definitely not a subset of your_set.

print(my_set.issuperset(your_set)) # gives us False,
# my_set does not encompass all of your_set.

