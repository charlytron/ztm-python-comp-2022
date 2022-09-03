##############################################################################
#                              Break, Continue, Pass                         #
##############################################################################

# Break
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Break is used to break out of a loop
# for item in my_list:
#     print(item) # prints each item in the list
#     break

# we can also use a while loop to do the same thing

# a = 1
# while a < len(my_list):
#     print(a) # prints 0 to 4
#     a += 1
#     break

# There are two other keywords that can be used in loops
# Continue and Pass

# Continue
# Continue is used to skip the current iteration of the loop
# for item in my_list:
#     print(item) # prints each item in the list
#     # break
#     continue

# a = 1
# while a < len(my_list):
#     print(a) # prints 0 to 4
#     a += 1
#     # break
#     continue

#  Why do we even need Continue?
#  We can use it to skip over certain items in a list

# for item in my_list:
#     continue # goes bqck to the top of the loop
#     print(item) # prints nothing

# a = 1
# while a < len(my_list):
#     a += 1
#     continue # goes back to the top of the loop
#     print(my_list) # prints nothing
    
# Pass
# Pass is used to do nothing
# It is used as a placeholder

a = 1
while a < len(my_list):
    print(my_list[a]) # prints 4
    a += 1
    pass # does nothing, passes to the next line
    # good to have as a placeholder

for item in my_list:
   # thinking about what to do next
    pass