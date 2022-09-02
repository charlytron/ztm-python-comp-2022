######################################################################
#                         range() function                          #
######################################################################
 
#  range() function is an inbuilt function in Python 3, which is used to generate a sequence of numbers over time.   

print(range(100)) # prints range(0, 100)))    

# Used mostly in for loops; we can iterate over a sequence of numbers using range() function.

for number in range(10):
    print(number) # prints 0 to 9

# Why is this useful? Let's say we want to print the numbers 1 to 10. We can do this,
# allowing us to loop as many times as we want.

for number in range(1, 11):
    print('email email list') # prints 1 to 10

# If we don't need the variable, we can use an underscore instead.

for _ in range(1, 11):
  print(_) # prints 1 to 10 because we just need to loop 10 times

# Range also has a third parameter, which is the step size. This is the number of
# steps we take between each iteration.

for number in range(1, 11, 2):
  print(number) # prints 1, 3, 5, 7, 9

# What if we step backwards?

for number in range(0, 10, -1):
  print(number) # doesn't work because we are stepping backwards

for number in range(10, 0, -1):
  print(number) # prints 10 to 1

for number in range(10, 0, -2):
  print(number) # prints 10, 8, 6, 4, 2

# We can also use range() to create a list of numbers.d

numbers = list(range(1, 10))
print(numbers) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in range(2):
  print(list(range(10))) # prints 2 lists of 10 numbers