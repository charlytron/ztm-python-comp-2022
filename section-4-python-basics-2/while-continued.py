##############################################################################
#                          While Loops Continued                            #
##############################################################################

# While loops are useful when we don't know how many times we want to loop.

a = 0

while a < 10:
    print("hello") # prints Hello infinitely
    a += 1 # a = a + 1
else: # will only execute if the while loop is not interrupted with break
    print("Done")    # Breaks out of the loop

# When should we use a while loop, and when should we use a for loop?
# It depends on the situation. If we know how many times we want to loop, we should
# use a for loop. If we don't know how many times we want to loop, we should use a
# while loop.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in my_list:
    print(item) # prints each item in the list

# we can also use a while loop to do the same thing

a = 1
while a < len(my_list):
    print(a) # prints 0 to 4
    a += 1

# For loops are simpler to use, but while loops are more flexible.
# One of the most useful ways to use a while loop is to loop until a condition is met.

while True:
    response = input('Say something: ')
    if (response == 'bugger off'):
        break