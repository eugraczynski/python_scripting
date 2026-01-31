my_list = [1, 2, 3]
my_list.reverse()
new_list = my_list[::-1] # Result: [3, 2, 1]
list(reversed(my_list))



def function_list(list_func, nums):
    return list_func(nums)

def list_func(num: list) -> list:
    return num.reverse()