from typing import Callable


nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda is anonymous function

# high-order functions: functions that take other functions as arguments
# e.g. passing function as an argument to another function
def function_list(list_func: Callable[[list[int]], list[int]], nums: list[int]) -> list[int]:
    return list_func(nums)

def list_func(num: list[int]) -> list[int]:
    return list(reversed(num)) # or nums[::-1]



print(function_list(list_func, nums_list))

# the same way using lambda you can pass function as an argument
print(function_list(lambda x: list(reversed(x)), nums_list))  


# filter keeps only speciefic values, like, dividable by 2
a = list(filter(lambda x: x % 2 == 0, nums_list))

# map apply to each element of a list
# map object needs to be converted to list type
b = list(map(lambda x: x * 2, nums_list))

print(a,b)
