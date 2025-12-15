from z1 import z2_outscoped
# import z1 as aliaso

# print(aliaso.__name__)
# print(aliaso.__file__)
# aliaso.z2_outscoped()

print(z2_outscoped())

print(globals())

if "z2_outscoped" in globals():
    print("yes")
