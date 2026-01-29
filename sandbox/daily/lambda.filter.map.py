nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# high-order functions: functions that take other functions as arguments
list(filter(lambda x: x % 2 == 0, nums_list))
list(map(lambda x: x * 2, nums_list))