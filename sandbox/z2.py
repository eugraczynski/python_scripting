# from z1 import z2_outscoped
import z1

print(z1.__name__)
print(z1.__package__)
# print(aliaso.__file__)
# aliaso.z2_outscoped()

# print(z2_outscoped())
print(z1.__x)
# print(globals())

if "z2_outscoped" in globals():
    print("yes")
