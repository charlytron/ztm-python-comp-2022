###############################################################################
#                                 SETS                                        #
###############################################################################

# Sets are unordered collections of unique elements.
# Sets are mutable (can be changed) and un-indexed (can't be accessed by index).

# my_set = {1,2,3,4,5}
# print(my_set) # gives us {1,2,3,4,5}

# my_set2 = {1,2,3,4,5,5} # gives us {1,2,3,4,5}
# print(my_set2) # gives us {1,2,3,4,5}, duplicates are removed

# my_set.add(100) # adds 100 to the set
# print(my_set) # gives us {1,2,3,4,5,100}
# there's no bookshelf that would place all of these together in memory.
# it's just a set of unique elements.
# But a set is able to find them because they're all unique.


# my_list = [1,2,3,4,5,5]
# set(my_list) # gives us {1,2,3,4,5}
# constrains the elements to be unique.

# print(set(my_list)) # gives us {1,2,3,4,5}, replacing parentheses with curly braces

# when would this be useful?
# when you want to find the unique elements in a list.

# Imagine we have usernames or emails and we don't want to have duplicates.
# We might want to convert a list of usernames or emails to a set.

my_set = {1,2,3,4,5,5}
# print(my_set[0]) # set objects are unindexed, so we can't access them by index.
print(1 in my_set) # gives us True
print(len(my_set)) # gives us 5, the length of the set, but it only counts unique elements.

# We can also convert the set into a list.
print(list(my_set))

new_set = my_set.copy() # gives us {1,2,3,4,5}
my_set.clear() # gives us None, removing all keys and values from the dictionary.
print(new_set) # gives us {1,2,3,4,5}
print(my_set)  # gives us set() because we cleared the set.




