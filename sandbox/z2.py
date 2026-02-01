import z1

print(z1)
print(globals())
# print(z1.__package__)
# print(aliaso.__file__)
# aliaso.z2_outscoped()

# print(z2_outscoped())
# print(globals())

if "z2_outscoped" in globals():
    print("yes")


if __name__ == "__main__":
    z1.main()
