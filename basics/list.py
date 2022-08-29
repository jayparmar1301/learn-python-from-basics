"""""""""""""""""""""""""""""""""""""""""
# list is python data structure used for storing elements with multiple data types
"""""""""""""""""""""""""""""""""""""""""
## list used [] to store elements
simple_list_with_values = [1,3,4,5,6,3,4,4]

# list has variety range of in build functions which we can use
# sort() method will sort all element in acending order
simple_list_with_values.sort()

# append() method is used to add new elements in existing list
simple_list_with_values.append(33)

# copy() method used for copying main list as copy to new list
simple_list_with_values.copy()

# count() method will gives us num of occurrence that particular element has
# let say simple_list_with_values list, occurrence of 4 is 3 times so it will return 3 
simple_list_with_values.count(4)

# index() method will return index of given element
# note: if same element occurred 2 times in list then it will only return first index
simple_list_with_values.index(4)

# pop() method will remove last element from list
simple_list_with_values.pop()

# remove() method will remove particular element from list
simple_list_with_values.remove(4)

# reverse() method will reverse list
# [1,3,4,5,6,3,4,4] -> [4,4,3,6,5,4,3,1]
simple_list_with_values.reverse()

# extend() method used to string one-by-one into list
# ("123") -> [1,2,3] in existing list
simple_list_with_values.extend("123")

# clear() method will remove all elements from list
simple_list_with_values.clear()

# find length of list, we have two ways
len(simple_list_with_values)
simple_list_with_values.__len__()

# multiple list, it multiple itself with count we gave
# [1, 3] * 2 -> [1,3,1,3]
simple_list_with_values.__mul__(2)
simple_list_with_values * 2

## list with different data type
list_with_multiple_data_type = [1, "Hey", 30.10, -1, "there!"]
# note: .sort() will not work with multiple data type
