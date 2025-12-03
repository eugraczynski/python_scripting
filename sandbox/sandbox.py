from typing import Sequence
from faker import Faker
import re
import sys
# import os


from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


# print(os.getcwd())
# print(sys.path)


var_underscore = 123


# references
a = 1
b = 2
a, b = b, a

x = a
print(a)
# a = a + 1
print(a)
print(x)

print(id(x))
print(id(a))

print(x is a)  # comparator of references

n = None
n1 = None
print(n is n1)  # they reference to same object

lst = [1, 2, 3, 4]
print(id(lst))
lst.append(5)
print(lst)
print(id(lst))


x, y = 1, 2  # tuple unpacking
tuple_s = 1, 2, 3

(1, 2) + (3, 4)
# returns (1,2,3,4)

# # iterable == colletion == Sequence()
s = "longstring"
for index, values in enumerate(s):
    print(index, values)

# to stop iterating when value found,
for x in range(10000):
    if x == 200:
        print("found 200")
        break


# while True:  # will run forever unless break
#     print("time!")

# enumerate()
# enumerate?  - can be used in python jupiter

# 1 + 2, adds two objects(python based on objects)
# for both stored object, and merges them, creating third object and reference to it

# amount of references to exact object variable
# print(sys.getrefcount(a))


# mutable, immutable

# mutable - can be changed after creation
# [list] { dic: val, dic2: val } sets { 1, 2, 3}
# immutable can't be changed
# Numbers, strings, tuples, frozenset


# number types are:
# int, float, complex(?)


# transforming types
listed_characters = list("word")
print(listed_characters)
# ['w', 'o', 'r', 'd']


# random.shuffle(list_var)


fake = Faker()


lorem = (
    "Contrary to popular belief, "
    "Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin "
    "literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor "
    "at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, "
    "from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered "
    'the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" '
    "(The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, "
    'very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", '
    "comes from a line in section 1.10.32."
)


x = re.search("[Ll]orem", lorem)

# if x:
#     print("Match found")
# else:
#     print("No match found")

# print(re.findall(r"Ext\w*m.s", lorem))

# <_>
#
# Person Class
# -name: string
# -address: string
# -email: string
# <<create>>+__init__(name: string, address: string, email: string)
# +__str__(): string
# +get_name(): string


class Person:
    def __init__(self, *name: str, address, **email: str):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\n"

    def get_name(self):
        return self.name


# person = Person(fake.name(), fake.address(), fake.email())

person = Person(
    fake.name(), fake.name(), fake.name(), address=fake.address(), email=fake.email()
)

# print(person)
# print("Person's Name:", person.get_name())


# print(fake.address())
# print(fake.currency_code())

# <_>

# print("car" in ["car", "bus", "train"])
# test_ in pytest
# immutable structure
# error handling
# print([x * 2 for x in [1, 2, 3]])

# aspice
# (Python, CAN tools, automation logs)
