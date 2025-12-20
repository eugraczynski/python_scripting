# Dictionary iteration
# %%
data = {"key1": 25, 100: "value100", "cadabra": "abra", (1,2): (3,4), "shmobject": object, False: None}
# print(data.items()) return list of tuples
[print(key, value) for key, value in data.items()]
[print(key) for key in data.keys()]
[print(value) for value in data.values()]
print(dict([(value, key) for key, value in data.items()]))
# or 
{key: value for key, value in data.items()}

# List manipulation

# Set manipulation

# Tuple manipulation
