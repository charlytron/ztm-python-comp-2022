############################################################
#                String Indices (indexes)                  #
############################################################

# String indices are the positions of the characters in a string.

wolfe = 'mau mau and the flak catchers'
       # 0123456...

# Each character will be stored in memory at a certain position.
# including the space character, there are 26 characters in the string.
# The computer will search within the shelf from 0 to 25.

print(wolfe[0]) # m
print(wolfe[23]) # t
print(wolfe[7]) # space

# [start:end:step]
# [0:3] will print the first three characters.

sequence = '01234567'
print(sequence[0:3]) # 012
print(sequence[0:3:2]) # 02 step by 2
print(sequence[1:]) # 1234567
print(sequence[:]) # 01234567
print(sequence[:5]) # 01234
print(sequence[::1]) # 01234567
print(sequence[::2]) # 0246
print(sequence[-1]) # 7
print(sequence[-3]) # 5
print(sequence[::-1]) # counts backwards from the end of the string
print(sequence[::-2]) # counts backwards by 2s from the end of the string