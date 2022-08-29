############################################################
#                  LIST METHODS 3                          #
############################################################

basket = [1, 8, 3, 9, 5]
# basket.sort() # gives us None because it's a method that modifies the list in place.
print(basket) # gives us [1, 3, 5, 8, 9]

# If we go to built-in functions, we can see that there is a sorted() function.

sorted(basket) # gives us [1, 3, 5, 8, 9]. It produces a new list.
print(sorted(basket))
print(basket) # gives us [1, 8, 3, 9, 5]

# sorted() creates a new copy of the basket list and sorts it.

new_basket = basket[:] # creates a new copy of the basket list.
new_basket.sort()
basket.reverse() # modifies the original list.
print(basket) # gives us [5, 9, 3, 8, 1]

