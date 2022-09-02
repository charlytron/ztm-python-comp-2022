##############################################################################
#                                WHILE LOOPS                                #
##############################################################################

# While loops are used to execute a set of statements as long as a condition is
# true.

# While loops are useful when we don't know how many times we want to loop.

a = 0

while a < 10:
    print("hello") # prints Hello infinitely
    a += 1 # a = a + 1
else: # will only execute if the while loop is not interrupted with break
    print("Done")    # Breaks out of the loop
