##############################################################################
#                                Our First GUI                               #
##############################################################################

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '$'
empty = ' '


def show_tree():
    # iterate through each row in the picture
    for row in picture:
        for pixel in row:
            if (pixel):  # shortening of if pixel == 1:
                print(fill, end='')
            else:
                print(empty, end='')
        print('')


show_tree()
print(show_tree) # prints the memory address of the function
