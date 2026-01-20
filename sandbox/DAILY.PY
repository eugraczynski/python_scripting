# Dictionary iteration
# %%
data = {"key1": 25, 100: "value100", "cadabra": "abra", (1,2): (3,4), "shmsosbject": object, False: None}
# print(data.items()) return list of tuples
# [print(key, value) for key, value in data.items()]
# [print(key) for key in data.keys()]
# [print(value) for value in data.values()]
# print(dict([(value, key) for key, value in data.items()]))
# # or 
# {key: value for key, value in data.items()}

# List manipulation
list_o = [ key for key in data.keys() ]
print(frozenset(list_o))

# Set manipulation
set_ = { (key, value) for key, value in data.items() }
print(set_)

# Tuple manipulation
list_ = [(key, value) for key, value in data.items()]

print(hash(frozenset(list_)))
print(hash(tuple(list_)))
# print(hash(bytes(list_)))

import time
def time_dec(base_func):
    def wrapper():
        start = time.time()
        base_func()
        end = time.time()
        print(f"Function '{base_func.__name__}' executed in {end - start:.10f} seconds")
        print(f"1nd decorator executed {time.time()}")
    return wrapper

def another_deco(base_func):
    def wrapper():
        base_func()
        print(f"2nd decorator executed {time.time()}")
    return wrapper

@another_deco
@time_dec
def primary_func():
    return [key for key in data.items()]

primary_func()
