"""""""""""""""""""""""""""""""""""""""""
# tuple is immutable python data structure used for storing elements with multiple data types
# we cannot edit tuples once they are created, however we can concat two tuples
"""""""""""""""""""""""""""""""""""""""""

# tuple uses () symbol
simple_tuple = (1,3,0,5)

# sort() method will sort all element in acending order
simple_tuple.sort()

# index() method will return index of given element
simple_tuple.index(1)

# + opertor and __add__() method can be used to add tuples into tuple
simple_tuple += (4,5) 
simple_tuple.__add__(simple_tuple)

# find length of tuple, we have two ways
len(simple_tuple)
simple_tuple.__len__()

# hash() method accept objects and return hash value in integer
simple_tuple.__hash__()