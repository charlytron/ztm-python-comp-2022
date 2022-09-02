################################################################
#                        ENUMERATE                             #
################################################################

# enumerate() is a built-in function that returns an enumerate object.

for char in enumerate('hello'):
    print(char) # prints each character in the string, preceded by its index
    # (0, 'h')
    # (1, 'e')
    # (2, 'l')
    # (3, 'l')
    # (4, 'o')

for i, char in enumerate('hello'):
    print(i, char) # prints each character in the string, preceded by its index
    # unpacking the tuple above
    # 0 h
    # 1 e
    # 2 l
    # 3 l
    # 4 o

# We could do the same in the context of a list:
for i, char in enumerate(['a', 'b', 'c']):
    print(i, char) # prints each character in the list, preceded by its index
    # 0 a
    # 1 b
    # 2 c

# And also thusly with a tuple:
for i, char in enumerate(('a', 'b', 'c')):
    print(i, char) # prints each character in the tuple, preceded by its index
    # 0 a
    # 1 b
    # 2 c

for i, char in enumerate(list(range(100))):
  print(i, char) # prints each number in the list, preceded by its index
  if char == 50:
      print(f'index of 50 is: {i}') # prints the index of 50
      # index of 50 is: 50