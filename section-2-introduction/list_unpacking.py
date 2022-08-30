############################################################
#                  LIST UNPACKING                          #
############################################################

# We can unpack a list into multiple variables.

basket = [1,2,3]

# What about assigning a variable to each element of the list?

a, b, c = basket

# or...

# a, b, c = [1,2,3]

# print(a) # gives us 1
# print(b) # gives us 2
# print(c) # gives us 3# 

# This is where list unpacking gets really useful.

# a,b,c = [1,2,3,4,5,6,7,8,9]

# what if we wanted to unpack 1,2,3 but keep the rest of the list?

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a) # gives us 1
print(b) # gives us 2
print(c) # gives us 3# 

print(other) # gives us [4, 5, 6, 7, 8, 9]
print(d) # gives us 9

# We're able to unpack our list however we want.

############################################################

