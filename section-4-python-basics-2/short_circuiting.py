###############################################################################
#                              Short Circuiting                               #
###############################################################################



is_Friend = True
is_User = True

# print(is_Friend and is_User) # True# 

if is_Friend and is_User:
    print("You are allowed to message")

# Short circuiting is a technique that allows us to avoid unnecessary computation
# if a condition is not met.

if is_Friend or is_User:
    print("You are allowed to message")

# Which operation is more efficient?
# The second operation is more efficient because it doesn't need to check if the
# condition is met. If the first condition is already false, the second condition
# is not even evaluated. The interpreter has already done enough work.

