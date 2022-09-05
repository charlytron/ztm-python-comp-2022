##############################################################################
#                      Function Exercise - 1                                 #
##############################################################################

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def highest_even(li):
    evens = [] # create an empty list to store the even numbers
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even(li)) # 10