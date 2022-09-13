"""""""""""""""""""""""""""""""""""""""""
# dictionary is python data structure used for storing elements with multiple data types
# data stored is stored as key-value pair in dictionary, we can access dictionary using key
"""""""""""""""""""""""""""""""""""""""""
## dictionary used {} to store elements
simple_dict = {"key":"value"}

# dictinary has variety range of in build functions which we can use
# pop() method will remove key element from dictinary
simple_dict.pop("key")

# popitem() method will last key-value pair element from dictinary
simple_dict.popitem()

# update() method will update value for given key in dictinary
# syntax will be your_dict.update(key=new_value), key is without quotes
simple_dict.update(a=2)
simple_dict.update(a=2,b=3)

# add new element in existing dictionary
simple_dict["new_key"] = "this is new value"

# copy() method used for copying main dict as copy to new dict
copy_dict = simple_dict.copy()

# get() method will return value of requested key and if not present then will return None
simple_dict.get("new_key")

# setdefault() method add key without default value in dict
simple_dict.setdefault('salary')
#output {'a': '2', 'b': 3, 'salary': None}

# items() method will gives us iterable key-value pairs from dict
for key, value in simple_dict.items():
    print(key, value)

# keys() method will only keys from dict
for key in simple_dict.keys():
    print(key)

# values() method will only value from dict
for value in simple_dict.values():
    print(value)

# clear() method will remove all elements from dict
simple_dict.clear()

# fromkeys() method will create new key value pair in given sequence 
keys = {"a", "b", "c"}
values = 1
simple_dict = dict.fromkeys(keys, values)
# output: {'a': 1, 'b': 1, 'c': 1}

# to find length of dict, we have two ways
len(simple_dict)
simple_dict.__len__()

## dict with different data type
dict_with_multiple_data_type = {"int_key": 1, "str_key": "hey, there!", "float_key": 30.0}
