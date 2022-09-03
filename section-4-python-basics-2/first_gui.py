##############################################################################
#                                Our First GUI                               #
##############################################################################

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
    # iterate through each row in the picture
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')

show_tree()
