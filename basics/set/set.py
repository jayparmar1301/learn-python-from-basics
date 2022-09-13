"""""""""""""""""""""""""""""""""""""""""
# set is one of 4 built-in data types in Python used to store collections of data
# set is different from tuple as it is mutuable and unordered in nature
"""""""""""""""""""""""""""""""""""""""""

#  set uses {} symbol same as dictionary but does not stored as key-value pair
simple_set = {1,3,0,5}

# add() method can be used to add new values in set
simple_set.add(6)

# difference() method is used to find difference between two sets
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
result_set = simple_set1.difference(simple_set2)
# output {1,3} 
# note that if we use A - B then it will return elements of A that are not in B
# and if we use B - A then it will to vise-versa  

# difference_update() method is used to find in-place difference between two sets
# it won't create new sets as result, it will update existing one
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
simple_set1.difference_update(simple_set2)

# insertsection() method is used to find common values in both sets
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
result_set = simple_set1.insertsection(simple_set2)
# output {4, 5} 

# insertsection_update() method is used to find in-place common values in both sets
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
simple_set1.insertsection_update(simple_set2)
# output {4, 5} 

# isdisjoint() method check whether the two sets are disjoint or no and return true if it is disjoin else false
# disjoint set means both sets have no common value 
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
simple_set1.isdisjoint(simple_set2)
# output False

# issubset() method check whether the given set is subset or not and return true if it is else false
# subset means set 1 contains all values from set 2
# example: set1 = {2,3,5} set2 = {2,3}, so set2 is subset of set1 however set1 is not subset of set2
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
simple_set1.issubset(simple_set2)
# output False


# issuperset() method check whether the given set is superset or not and return true if it is else false
# set A is called the superset of another set B if all elements of set B are elements of set A
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
simple_set1.issubset(simple_set1)
# output True

# The symmetric difference of two sets set1 and set2 is the set of elements which are in either of the sets set1 or set2 but not in both.
simple_set1 = {1,3,4,5}
simple_set2 = {4,5}
simple_set1.symmetric_difference(simple_set1)
# output {1, 3}

# pop() method is used to remove last element from set
simple_set.pop()

# remove() method is used to remove specific value from set
# and if value is not present then it will raise error
simple_set.remove(1)

# discard() method is used to remove value from set
# difference in discard method is that it will not raise error even if key is not present
simple_set.discard(1)