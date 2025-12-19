# from typing import Sequence
# from faker import Faker
# import re


# import os
import argparse
import re
# import cantools
# import zipfile
# import pathlib
# import os
# import re
# import xml.etree.ElementTree as ET

# Python is strongly typed language
# you cant add 1 + '1' and expect it to work

# Some variables are also built-in python functions like 'list'
# each time we create variable with same name we override it
# so instead of 'list', 'list_' is suggested as naming convention


# jupyter - instal extention so you can run small chunks of code
# just click run cell, starts with # %%


# import json
# key = '{ "key": "value", "key": "value", "key": "value"}'

# key2 = {'keys':'val'}
# key2['pair'] = 'ars'

# keisy = str({"1":"1"})
# # print(keisy)

# add = { "key1": "pair3" }
# myvar = json.loads(key)
# myvar.update(add)


# a = 15
# print("Hello! " * 2)

# print(json.dumps(myvar))

# with open('dict.json', 'r') as dict:
#     filejson = json.loads(dict.read())
#     filejson.update(add)


# with open('dict.json', 'w') as json_final:
#     json_final.write(json.dumps(filejson))


#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         return print('exit!')

# with ZipHelper('swad', 'pack') as zipAlias:
#     print(zipAlias.get_name())

# try:
#     for dirpath, dirname, filenames in os.walk(self.path):
#         for filename in filenames:
#             filepath = os.path.join(dirpath, filename)
#             os.remove(filepath)
# finally:
#     for dirpath, dirname, filenames in os.walk(self.path):
#         for dir in dirname:
#             folderpath = os.path.join(self.path, dir)
#             os.rmdir(folderpath)

# def xml_changer():
#     tree = ET.parse("./extracted_tasks/task1/DataSetB.xml")
#     root = tree.getroot()

#     # itered = root.iter("Signal")
#     # print('DEBUG - Itered by "Signal":\n', itered)
#     notitered = root.findall('.//TxMessage/Signal[@name="Temperature"]')
#     # print("DEBUG - Itered by findall(//path/to/file'):\n", notitered)

#     root.append(
#         ET.Element(
#             "Signal",
#             attrib={
#                 "name": "Last Signal",
#                 "datatype": "int",
#                 "unit": "units",
#                 "offset": "0",
#             },
#         )
#     )

#     def pew(elem):
#         elem.attrib["name"] = "HOTHOTHOTHOT"
#         root.find(".//TxMessage").append(
#             ET.Element("Signal", attrib={"name": "NewSignal"})
#         )

#     for elem in notitered:
#         # ternary
#         pew(elem) if elem.attrib["name"] == "Temperature" and elem.attrib[
#             "datatype"
#         ] == "float" and elem.attrib["unit"] == "Celsius" and elem.attrib[
#             "offset"
#         ] == "0" else notitered.remove(elem)

#     # should be at the end of file to apply indentation to whole xml
#     ET.indent(tree, space="    ", level=0)

#     root.append(ET.Element("Tail", attrib={"MyTail": "MyRules"}))
#     root.tail = "\n\nthis is tail, hi"
#     tree.write("./DataSetB_modified.xml")


# def db_checker():
#     db = cantools.database.load_file("./extracted_tasks/task1/DataSetC.dbc")
#     answer = db.messages
#     # print(db)

#     get_message = db.get_message_by_name("ControlCommand")
#     print(get_message.signals)

#     for ans in answer:
#         # print('Full answer - ', ans)
#         for signal in ans.signals:
#             print(
#                 signal.name,
#                 signal.start,
#                 signal.length,
#                 signal.conversion.scale,
#                 signal.minimum,
#                 signal.maximum,
#                 signal.unit,
#                 signal.receivers,
#             )


# argparse section
parser = argparse.ArgumentParser(description="Process some tasks.")
parser.add_argument("-z", "--zoo", help="Print animals")
parser.add_argument("-n", "--numerics", help="Numeric sum", type=float, nargs="*")
parser.add_argument(
    "-v",
    "--verbose",
    type=int,
    choices=[1, 2, 3],
    help="Enable verbose output 1, 2, 3 etc.",
)
parser.add_argument("--unpack", action="store_true", help="Unpack the zip files")
parser.add_argument("--checkdb", action="store_true", help="Check the DBC file")
parser.add_argument("--changexml", action="store_true", help="Change the XML file")
parser.add_argument(
    "--pack", action="store_true", help="Pack the modified files into a zip"
)

args = parser.parse_args()

# # print(args)

# if args.numerics is not None:
#     print(f"Numeric inputs: {args.numerics}")
#     print(sum(args.numerics))

# if args.checkdb:
#     db_checker()

# if args.changexml:
#     xml_changer()

# if args.pack:
#     pack_the_zip()

# if args.verbose is not None:
#     match args.verbose:
#         case 1:
#             print("Verbose level 1 enabled")
#         case 2:
#             print("Verbose level 2 enabled")
#         case 3:
#             print("Verbose 3 enabled")
#         # never called because of argparse choices
#         case _:
#             print("Wrong verbose input")

# if args.zoo is not None:
#     match args.zoo:
#         case "cats" | "cat":
#             print("Meow! Meow!")
#         case "dogs":
#             print("Woof! Woof!")
#         case "birds":
#             print("Chirp! Chirp!")
#         case _:
#             print("That's not an animal. \nBut you are!")


# # unpack_the_zip()
# # db_checker()
# # xml_changer()
# # pack_the_zip()


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

lorem = """Contrary to popular belief,
    Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin
    literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor
    at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur,
    from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered
    the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum
    (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, 
    very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet.., 
    "comes from a line in section 1.10.32."""


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
# def methodName(a):
#     a = str(a)
#     i = len(a)
#     answer = 0
#     for n in a:
#         answer = answer + int(n) ** i
#     return answer == a


# print(methodName(1634))

# print(3**3.0)

# list_ = [[]] * 5
# print(list_)
# list_[0].append(1)
# print(list_)


# def foo(x):
#     f1 = lambda: x
#     x = 20
#     f2 = lambda: x
#     x = 30
#     f3 = lambda: x
#     return f1, f2, f3


# [f() for f in foo(10)]


# class A:
#     x = "a"

# class B:
#     x = "b"


# class C:
#     pass


# C.__mro__ = (A, object)
# print(C().x)


# x, y, z = True, False, False
# print(x or y and z)

# print(["Andrew", "Chris", "Craig", "Duncan"][-1][-1])


# class A:
#     __attr = "A"


# class B(A):
#     __attr = "B"


# print(B().__attr)


# from encap import *

# print(_A().method(), _A()._method())


# len(x for x in range(1, 5) if x % 2)


# class A:
#     a = 10
#     b = a
#     c = [a + i for i in range(3)]


# obj = A()
# print(obj.a, obj.b, obj.c)


# class A:
#     a = 10
#     b = a
#     c = []
#     for i in range(3):
#         c.append(a + i)


# obj = A()
# print(obj.a, obj.b, obj.c)


# print(0b10 + 0o10 + 0x10)

# f = lambda x, y: x + y, x - y
# f(10, 5)


# def boo():
#     func = lambda: x
#     x = 5
#     return func


# print(boo()())

# a, (b, (c,)) = [1, (2, {3: 4})]


# x = a, (b, (c, d)) = [1, (2, {3, 4})]
# print(x)

# list_ = [1, 2, 3, 4]
# list_[3:1] = 0
# print(list_)


# list_ = [1, 2, 3, 4]
# list_[3:1] = "?"
# print(list_)


# lists = [[1, 2, 3], ["a", "b", "c"]]
# labels = []
# result = []

# for list_ in lists:
#     reversed_list = reversed(list_)
#     if not labels:
#         labels = ["ITEM %s" % i for i in reversed_list]
#     result.append(list(reversed_list))

# print(result)

# you can append one elements of the list

# x = [1, 2, 3]
# x.append(4)
# print(x)

# but for multiple-value list append - use extend

# x = [1, 2, 3]
# x.extend([4, 5])
# print(x)


# print(dir("str"))

# isnumeric() and isdigit()

# %%
print(dir(__builtins__))

# %%
len("\n")  # length is 1

# %%
len(r"\n")  # length is two

# %%

list_ = [None, 1, 2, 3]
# list_.__len__()
list_[-1]
# print(list_.copy())
# %%
len([1, 2, 3, *range(100)])

# result is 103 (?)

# appending to the array / list is faster then pre-pending at the beginning
# for python adding at the end is easier then before
# %%

a = [1, 2, 3, 4, 5, 6]
a[-3:-1]
# template is [from:to]
# %%
id(list_)
# %%
list_.append(1)
id(list_)

# %%
list_.count(1)
# %%
1 in list_

# %%

# print(f"{id(list_)} shallow: {id(list_.copy())} deep: {id(list_.__deepcopy__())} ")

# %%
# produces empty list
x = list()

# %%
x = bool()
# %%

# set is a collection of unique elements
# s = set()
# %%
s = {4, 2, 3, None}
print(s)
# %%
s.add(1)
print(s)
# %%
s.add(1)
print(s)
# %%
s.update({0, 1, 1})
print(s)
# %%
from logging.config import valid_ident
import sys

print(sys.getsizeof(s))
# %%
d1 = {"a": "1"}
# %%
d2 = {"b": "2"}
# %%
d1.update(d2)
print(d1)
# %%

# if else logic can be done via dictionaries
options = {"case1": "1", "case2": "2", "case3": "3"}
x = "case2"
if x in options:
    print(x)

# %%
options = {"case1": "1", "case2": "2", "case3": "3"}
# %timeit 9999999 in options

# SET() are very fast

# {<CONTRACT> : {INIT: 4, COMPLETED: 2}}
# result = {}
# for row in options:
#     key = (row["name"], row["contract"])
#     result[key] = result.setdefault(key, 0) + row["qty"]
# %%
print(type({"a": 1}))
# int("abc")

# %%

for x in range(1, 11):
    for y in range(1, 11):
        print(x * y)
    print()


# %%
def draw_table():
    result = ""
    for x in range(1, 11):
        for y in range(1, 11):
            result += f"{x * y:4}"
        result += "\n"
    return result


print(draw_table())
# %%
list_ = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]


answer = []


def func(item):
    print(item)
    if isinstance(item, list):
        return answer.append(item)


map(func, list_)
print(answer)

# %%


def rec_func(nested_list):
    answer = 0
    for item in nested_list:
        if isinstance(item, list):
            answer += rec_func(item)
        else:
            answer += item
    return answer


print(rec_func(list_))


def nested_sum(nested_list):
    return sum(nested_sum(x) if isinstance(x, list) else x for x in nested_list)


print(nested_sum(list_))


# %%
def find_lambda(list_):
    answer = []
    for item in list_:
        if callable(item):
            list_.remove(item)
            for j in list_:
                answer.append(item(j))
    return answer


print(find_lambda([lambda a: a + 2, 9, 3, 1, 0]))  # [11, 5, 3, 2]
print(find_lambda([9, 2, 3, lambda a: a / 2.0, 1, 0]))  # [4.5, 1, 1.5, 0.5, 0.0]


# map(lambda x: func(list_[list_.index(x)]), list_)
# y = list(map(lambda x: list_.remove(x) if callable(x) else x), list_)
# %%
# for 2+ lambdas in lists
def find_lambda(list_):
    answer = []
    lambda_list = []
    for item in list_:
        if callable(item):
            lambda_list.append(item)
            list_.remove(item)
    for func in lambda_list:
        for item in list_:
            answer.append(func(item))
    return answer


print(find_lambda([lambda a: a + 2, 9, 3, 1, 0, lambda a: a + 2]))  # [11, 5, 3, 2]
print(find_lambda([9, 2, 3, lambda a: a / 2.0, 1, 0]))  # [4.5, 1, 1.5, 0.5, 0.0]

# %%
print([x * 2 for x in [1, 2, 3]])
# %%


# Anagram detect
def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1.lower()) == sorted(str2.lower())


print(is_anagram("AbbA", "BBaA"))  # True
# %%

# Mystical Sort
SEPARATORS = ",;|\t"
test_string = "boom;dracula,apple|coca-cola|fate|Love and other stuff\tZoomba-yumba"


# newlist = [x.replace(";", ",") for x in list]
def testo_me(arg):
    x = arg
    for item in SEPARATORS:
        x = x.replace(item, ",")
    splitted = x.split(",")
    splitted.sort(key=lambda v: v.upper())
    return ",".join(splitted)


testo_me()

print(testo_me(test_string))


def test_me(s=test_string):
    return s


# print(test_string)

# %%
