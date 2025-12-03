# from typing import Sequence
# from faker import Faker
# import re
# import sys
# # import os


# Okay some quic notes that can help improve:
# 1.  for practical purpose add a try block on each action
# 2. It's better if you use pack and unpack in different methods or make the current one a better and clearer name, now it's a bit confusing
# 3. when trying to find a end/start of a string it's better to use endswith()/startwith() this way if the string have some issue on the index it might cause a issue, also better readability.
# 4. The currently method will only work if we give the directory straight, for eg: /mypath/files/myfile.zip will not work, but /mypath/files/ will work it is good idea to use os.path to check, for eg with os.path.isfile if it is the file then process to make the extraction/packing
# 5. right now if you nested zip file has the same names as the file in main it will replace them, for eg lets say you have a zip1 inside it there are 2 files, A.txt and zip2, inside zip2 there is also a A.txt so in this case it will replace the zip1 file. My suggestion would be to unzip into folders (same paths as in root zip) and clean up once task is done, or add a pre- or suffix
# 6. your cleanup will fail since you're sending the file name and not the file path, use os.path.join to add name with the dirpath
# 7.  In you pack, make it more dynamic so it can use the any and pack into a zip, also add option to what type, .zip, .7z, .tar etc
# 8. Move the class into different file to import it, and start a new Main


# If something is unclear let me know 🙂


# from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent))


# # print(os.getcwd())
# # print(sys.path)


# var_underscore = 123


# # references
# a = 1
# b = 2
# a, b = b, a

# x = a
# print(a)
# # a = a + 1
# print(a)
# print(x)

# print(id(x))
# print(id(a))

# print(x is a)  # comparator of references

# n = None
# n1 = None
# print(n is n1)  # they reference to same object

# lst = [1, 2, 3, 4]
# print(id(lst))
# lst.append(5)
# print(lst)
# print(id(lst))


# x, y = 1, 2  # tuple unpacking
# tuple_s = 1, 2, 3

# (1, 2) + (3, 4)
# # returns (1,2,3,4)

# # # iterable == colletion == Sequence()
# s = "longstring"
# for index, values in enumerate(s):
#     print(index, values)

# # to stop iterating when value found,
# for x in range(10000):
#     if x == 200:
#         print("found 200")
#         break


# # while True:  # will run forever unless break
# #     print("time!")

# # enumerate()
# # enumerate?  - can be used in python jupiter

# # 1 + 2, adds two objects(python based on objects)
# # for both stored object, and merges them, creating third object and reference to it

# # amount of references to exact object variable
# # print(sys.getrefcount(a))


# # mutable, immutable

# # mutable - can be changed after creation
# # [list] { dic: val, dic2: val } sets { 1, 2, 3}
# # immutable can't be changed
# # Numbers, strings, tuples, frozenset


# # number types are:
# # int, float, complex(?)


# # transforming types
# listed_characters = list("word")
# # print(listed_characters)
# # ['w', 'o', 'r', 'd']


# # random.shuffle(list_var)


# fake = Faker()


# lorem = (
#     "Contrary to popular belief, "
#     "Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin "
#     "literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor "
#     "at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, "
#     "from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered "
#     'the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" '
#     "(The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, "
#     'very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", '
#     "comes from a line in section 1.10.32."
# )


# x = re.search("[Ll]orem", lorem)

# # if x:
# #     print("Match found")
# # else:
# #     print("No match found")

# # print(re.findall(r"Ext\w*m.s", lorem))

# # <_>
# #
# # Person Class
# # -name: string
# # -address: string
# # -email: string
# # <<create>>+__init__(name: string, address: string, email: string)
# # +__str__(): string
# # +get_name(): string


# class Person:
#     def __init__(self, *name: str, address, **email: str):
#         self.name = name
#         self.address = address
#         self.email = email

#     def __str__(self):
#         return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\n"

#     def get_name(self):
#         return self.name


# # person = Person(fake.name(), fake.address(), fake.email())

# person = Person(
#     fake.name(), fake.name(), fake.name(), address=fake.address(), email=fake.email()
# )

# # print(person)
# # print("Person's Name:", person.get_name())


# # print(fake.address())
# # print(fake.currency_code())

# # <_>

# # print("car" in ["car", "bus", "train"])
# # test_ in pytest
# # immutable structure
# # error handling
# # print([x * 2 for x in [1, 2, 3]])

# # aspice
# # (Python, CAN tools, automation logs)


# # def extract_nested_zip(zippedFile, toFolder):
# #     """Extract a zip file including any nested zip files
# #     Delete the zip file(s) after extraction
# #     """
# #     with zipfile.ZipFile(zippedFile, "r") as zfile:
# #         zfile.extractall(path=toFolder)
# #     os.remove(zippedFile)
# #     for root, dirs, files in os.walk(toFolder):
# #         for filename in files:
# #             if re.search(r"\.zip$", filename):
# #                 fileSpec = os.path.join(root, filename)
# #                 extract_nested_zip(fileSpec, root)


# def narcissistic(test_number):
#     separated = str(test_number)
#     length = len(separated)
#     answer = 0
#     for elem in separated:
#         answer += int(elem) ** length
#     return answer == test_number


# Over-compressed solution
# def narcissistic(test_number):
#     separated = str(test_number)
#     num_digits = len(separated)
#     return test_number == sum(int(digit) ** num_digits for digit in separated)


# print(narcissistic(7))  # True
# print(narcissistic(371))  # True
# print(narcissistic(122))  # False
# print(narcissistic(4887))  # False
# print(narcissistic(152))


# def result():
#     seconds_in_year = 60 * 60 * 24 * 365
#     return len(str(seconds_in_year))  # insert correctly calculated variable


# print(result())
