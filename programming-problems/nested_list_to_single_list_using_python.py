def iterate_on_nested_list(input):
    """Recursively iterates over a nested list and returns a flattened list.

    Args:
        input (list): The nested list to be iterated over.

    Returns:
        list: A flattened list containing all elements from the nested list.
    """
    if not isinstance(input, list):
        return input
    else:
        nested_val = []
        for i in input:
            if isinstance(i, list):
                nested_val.extend(iterate_on_nested_list(i))
            else:
                nested_val.append(i)
    return nested_val


input1 = [1, [1, 3], [1, [2, [[[3]], 2]]]]
print(f"value of input1: {input1} \noutput of input1: {iterate_on_nested_list(input1)}")

input2 = [1, [[[[[[[[[2]]]]]]]]]]
print(f"value of input2: {input2} \noutput of input2: {iterate_on_nested_list(input2)}")

input3 = [1, [[[[[[[[[2]]]]]]]]], [1, 3], [1, [2, [[[3]], 2]]]]
print(f"value of input3: {input3} \noutput of input3: {iterate_on_nested_list(input3)}")
