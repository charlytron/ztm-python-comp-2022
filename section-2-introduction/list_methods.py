############################################################
#                 LIST METHODS EXPLAINED                   #
############################################################

# List methods are functions that operate on lists.
# We saw similar methods for strings:

# string.upper()
# string.lower()
# string.split()
# string.join()
# string.replace()
# string.find()
# string.count()
# string.startswith()
# string.endswith()
# string.len()

# We can also use list methods on lists:

basket = ['milk', 'bread', 'eggs', 'apples', 'bananas']
print(len(basket)) # 5

# Lists become powerful when methods are used.

# List/array methods:

# append() - adds an item to the end of the list.
# insert() - adds an item to the list at a specific index.
# remove() - removes an item from the list.
# pop() - removes an item from the list and returns it.
# push() - adds an item to the list at the end.
# clear() - removes all items from the list.
# reverse() - reverses the order of the list.
# sort() - sorts the list.
# copy() - copies the list.
# count() - counts the number of times an item occurs in the list.
# index() - returns the index of an item in the list.
# extend() - adds all items in a list to the end of the list.

##########################################
# adding an item to the end of the list: #
##########################################

# new_list = basket.append(100)
# print(new_list) # nothing is returned.
# print(basket) # ['milk', 'bread', 'eggs', 'apples', 'bananas', 100]

# assigning new_list to basket.append(100) makes the new_list none
# because append changes the original list.
# We have to write

# new_list = basket
# print(basket)
# print(new_list)

# After we've appended to the basket, then we can assign new_list to the basket.

###############################################
#            Inserting an item:               #
###############################################


# basket.insert(5, 'chips')
# print(basket) # ['milk', 'bread', 'eggs', 'apples', 'bananas', 'chips', 100]

# Note that insert() modifies the original list in place, it doesn't make a copy.

# new_list = basket.insert(5, 100)
# print(new_list) # nothing is returned.
# print(basket) # ['milk', 'bread', 'eggs', 'apples', 'bananas', 100]

############################################################
#                EXTENDING A LIST:                         #
############################################################

new_list = basket.extend([100, 101, 102])
# print(new_list) # nothing is returned.
# print(basket) # ['milk', 'bread', 'eggs', 'apples', 'bananas', 100, 101]

# Again, it doesn't make a copy. It just modifies the original list in place.

############################################################
#                REMOVING AN ITEM:                         #
############################################################

# basket.pop(0) # removes the first item in the list.
# print(basket) # ['milk', 'bread', 'eggs', 'apples', 'bananas', 100, 101, 102]

basket.remove(100) 
print(basket) # ['milk', 'bread', 'eggs', 'apples', 'bananas', 101, 102]

# We give this the value of the item we want to remove.
# With pop(), we can also give it an index to remove.

new_list = basket.remove(101)
print(new_list) # nothing is returned.

# Remove also works in place. It doesn't make a copy.

new_list = basket.pop()
print(new_list) # 102

# Why is 102 returned?
# Because pop() returns the item that was removed.

new_list = basket.clear()
print(new_list) # nothing is returned.
print(basket) # []