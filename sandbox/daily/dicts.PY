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

