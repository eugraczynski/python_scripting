# from typing import Sequence
# from faker import Faker
import enum
import grp
import re


# import os
import argparse
import time
# import cantools
# import zipfile
# import pathlib
# import os
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

# print(sys.getsizeof(s))
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


# Anagram detect
def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1.lower()) == sorted(str2.lower())


print(is_anagram("AbbA", "BBaA"))  # True
# %%

# Mystical Sort
SEPARATORS = ",;|\t"
test_string = "boom;dracula,apple|coca-cola|fate|Love and other stuff\tZoomba-yumba"


def testo_me(arg):
    x = arg
    for item in SEPARATORS:
        x = x.replace(item, ",")
    splitted = x.split(",")
    splitted.sort(key=lambda v: v.upper())
    return ",".join(splitted)


print(testo_me(test_string))

# %%
# key value swap in dict
data = {
    "key1": 25,
    100: "value100",
    "cadabra": "abra",
    (1, 2): (3, 4),
    "shmobject": object,
    False: None,
}


def dict_swap(arg):
    unhashable_types = [list, dict, object]
    data_copy = arg.copy()
    for key, value in arg.items():
        if type(value) in unhashable_types:
            del data_copy[key]
    # return dict([(value, key) for key, value in data_copy.items()])
    return {key: value for key, value in data_copy.items()}


print(dict_swap(data))

# Advanced task (#2 in tests)
tricky_data = {"cadabra": "abra", (1, 2): [3, 4], "oops": {}}
dict_swap(tricky_data)

# %%
# enumerate() return tuples of (index, value)
lsrere = [1, 2, 3, 4, 5]
[print(item) for item in enumerate(lsrere)]
# %%
# %%
d = {"a": 1, "b": 2, "c": 3}
print(d["a", "b"])
# %%
d = {2.0: "a", 1: "b", 0: "c"}
print(d[0])
# %%
d = {}
print(d.get(0, 0))
# %%
d = {0: "a", 1: "b", 2: "c"}
print(d[3])
# %%
d = {}
d.setdefault(0, []).extend("abc")
print(d)
print(len(d))
# %%
d = {x: y for x in "abc" for y in range(3)}
print(d)
# %%
d = {None: None, None: None, None: None}
print(len(d))
# %%
d = {None: None}
print(len(d))


# %%
def func():
    pass


print(type(func) == type(lambda: None))
callable(func)
# isinstance(func, types.FunctionType)
print(isinstance(func, type(lambda: None)))


# %%
def foo():
    return x


x = 5
print(foo())


# %%
def f1():
    return 42


f2 = lambda: 42


# %%
def func():
    print(42)


a = func()
print(a)
# %%
keys = ["a", "b", "c"]
values = [1, 2, 3]
{zip(keys, values)}
# %%
{keys: values for keys, values in zip(keys, values)}
# %%
filter(lambda x: x % 2 == 0, range(10))
# %%
list(filter(lambda x: x % 2 == 0, range(10)))
# %%
"""Task is to return the percent rated value of current battery capacity parsed from given string 
(let's assume it is some shell command's result).

Current level should be calculated as CurrentCapacity / MaxCapacity in percents. The resulting value should be like the following example:

61.41%

There are two ways:

Parse from LegacyBatteryInfo block - this is super easy. If you are beginner - try to get needed info from this line.
Parse from MaxCapacity/CurrentCapacity attributes - more complex task for more experienced programmers. If you want challenge - try to get information without using data from LegacyBatteryInfo block.
The result of the function should be in the form of the string: "XX.YY%" where XX.YY is the float number of percents with 2 digits after dot."""
# %%
data = """
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
"""
import re

# data = data.replace('\'', '"')
# print(re.findall(r"(?:\"|\')\w+.+\d", data))
x = re.findall(r"(?:\"|\')\w+.+\d", data)


# y = (item.replace("=", ":") for item in x)
# print(y)
# print(list(dict(y)))
# for u in y:
#     print(u)
#     tup = tuple(u)
#     print(tup)


def get_battery_level(data):
    max_capacity = re.search(r"\"MaxCapacity\"\:\s+\+(\d+)", data)
    current_capacity = re.search(r"\'CurrentCapacity\'\=\s+(\d+)", data)
    res = int(current_capacity.group(1)) / int(max_capacity.group(1)) * 100
    return f"{res:.2f}%"


get_battery_level(data)

# %%
"""
Task:
Write a function that gives all the ways to divide a list of at least two elements in two non-empty parts.

Each two non empty parts will be in a tuple
Each part will be in a string
Elements of a pair must be in the same order as in the original array.
Example:
>>> a = ["az", "toto", "picaro", "zone", "kiwi"]
>>> partlist(a)

[('az', 'toto picaro zone kiwi'), ('az toto', 'picaro zone kiwi'), ('az toto picaro', 'zone kiwi'), ('az toto picaro zone', 'kiwi')]
"""

# %%
test_data = ["az", "toto", "picaro", "zone", "kiwi"]


def partlist(list_):
    result = list()
    for iter, item in enumerate(list_):
        if iter != 0:
            start = ""
            end = ""
            for i in range(0, iter):
                start += " " + list_[i]
            for k in range(iter, len(list_)):
                end += " " + list_[k]
            result.append((start.strip(), end.strip()))
    return result
    # print(end)
    # print(result)


print(partlist(test_data))

# %%
# Group Anagrams
"""Task is to process all words from input sequence and return a list with lists from those words that are anagrams with others in their list

A typical test could be :

list_ = ["tsar", "rat", "tar", "star", "tars", "cheese"]
group_anagrams(list_)  # [["tsar", "star", "tars"], ["rat", "tar"], ["cheese"]]
NOTE: the order of words in resulted lists should follow the order of appearance."""

# %%
test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]


def group_anagrams(words):
    anagram = {}
    for word in words:
        str_ = "".join(sorted(word))
        if str_ in anagram:
            anagram[str_].append(word)
        else:
            anagram[str_] = [word]

    return list(anagram.values())


print(group_anagrams(test_list))
print(group_anagrams(["abbA", "boom", "Mobo", "AbAb"]))
# %%
import this


# %%
def func():
    print(42)


a = func()
print(a)


# %%
def f1():
    return 42


f2 = lambda: 42
# %%
a = []


def f(x, y):
    a.append("z")


f(a.append("x"), a.append("y"))

print(a)
# %%
# def func:
#     print(42)

# a = func()
# print(a)
# %%
# ZASHKWAR SECTION


def boo():
    func = lambda: x
    x = 5
    return func


boo()()
# %%
numbers = [1, 2, 3, 4]
numbers.append([5, 6, 7, 8])
len(numbers)


# %%
def gen(i):
    for x in range(i):
        if x < 3:
            yield x
        else:
            break
    else:
        yield 10


sum(list(gen(3))), sum(list(gen(10)))
# %%
len(x for x in range(1, 5) if x % 2)
# %%
a, (b, (c,)) = [1, (2, {3: 4})]
print(a, b, c)


# %%
class A:
    x = 1


class B(A):
    x = 2


class C(A, B):
    pass


print(C().x)


# %%
class A:
    x = 1


class B(A):
    x = 2


class C(A, B):
    pass


print(C().x)
# %%
list_ = [1, 2, 3, 4]
list_[1:3] = []
print(list_)
# %%
0b10 + 0o10 + 0x10
# %%
# def boo():
#     x = 5
#     func = lambda: x
#     del x
#     return func

# boo()()
# %%
# ?????????????????????????????? why
list_ = [[]] * 5
list_[0].append(1)
list_
# %%
x = 1
y = 2
z = 1

if x < y < z:
    print(x, end=" ")
    print(y, end=" ")
    print(z)


# %%
class A:
    a = 10
    b = a
    c = [a + i for i in range(3)]


obj = A()
print(obj.a, obj.b, obj.c)


# %%
class A:
    a = 10
    b = a
    c = [A.a + i for i in range(3)]


obj = A()
print(obj.a, obj.b, obj.c)


# %%
class A:
    attr = 10

    def __init__(self):
        self.attr = 20


print(A.attr, A().attr)
# %%


class CLS:
    attr = 10

    def __init__(self):
        self.attr = 20

    def called(self):
        return self.attr


inst = CLS()
inst.__dict__
inst.__getattribute__("attr")


# %%
class CLS:
    attr = 10

    def __init__(self):
        self.attr = 20

    def called(self):
        return self.attr


# %%
class A:
    def m(self):
        return "A"


class B(A):
    def m(self):
        return super().m() + "B"


print(B().m())


# %%
class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return A(self.value + other.value)

    def __str__(self):
        return "A, value: {}".format(self.value)


print(A(10) + A(20))


# %%
def func(arg1, arg2, /, arg3, *, arg4):
    print(arg1, arg2, arg3, arg4)


func(1, 2, arg3=3, arg4=4)


# %%
def func(arg1, arg2, *args, **kwargs):
    [print(item) for item in (arg1, arg2, args, kwargs.values())]
    print(*args)
    print(kwargs.items(), kwargs.keys(), kwargs.values())


func(1, 2, 4, 5, 6, 7, arg4=4, arg5=5)
# %%
a = [1, 2, 3]
print(*a)
# %%
import time


def decor(base_func):
    def wrapper():
        start = time.time()

        print("Before function call")

        base_func()

        print("After function call")

        print(
            f"start - end: {(time.time() - start):.9f}",
        )

        return "end"

    return wrapper


@decor
def funcky():
    print("INSIDE FUNCTION")


funcky()


# %%
# ENCAPSULATION
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # def __str__(self):
    #     return f"Name: {self.name}, Age: {self.__age}"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


person = Person("John Doe", 30)
print(person)

# print(person.__age) # AttributeError

person.__age = 35  # This will not change the actual age
print(person)

print(person.get_age())  # Accessing age via getter

person.set_age(35)  # Changing age via setter
print(person)


person.__age = 35  # This will not change the actual age, but do smth
# with variable itself??????
print(person)

print(person.__age)  # NO AttributeError


# %%
# Polymorphism
class DOG:
    def sound(self):
        return "Woof!"


class CAT:
    def sound(self):
        return "Meow!"


doggo = DOG()
catto = CAT()

for animal in (doggo, catto):
    print(animal.sound())


# %%
# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def name_info(self):
        return f"Animal's name is {self.name}"


class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"


doggo = Dog("Buddy")
catto = Cat("Whiskers")

print(doggo.bark())
print(catto.meow())
print(doggo.name_info())
print(catto.name_info())

params = ["a", "b", "c", "d"]
print(*params)
# %%
print(hash(42))  # int, hashable
print(hash(3.14))  # float, hashable
print(hash("hello"))  # string, hashable
print(hash(b"bytes"))  # bytes, hashable
print(hash(range(10)))  # range, hashable
print(hash(None))  # NoneType, hashable
print(hash(True))  # bool, hashable
print(hash(3 + 4j))  # complex, hashable
print(hash(bytes([1, 2, 3])))  # bytes, hashable
print(hash((1, 2)))  # tuple of immutable objects, hashable
print(hash((1, (2, 3), "four")))  # tuple of immutable objects, hashable
print(hash(()))  # empty tuple, hashable
print(hash(frozenset()))  # empty frozenset, hashable
print(hash(frozenset([1, 2, 3])))  # frozenset of immutable objects, hashable
print(hash((42, "answer", 3.14)))  # tuple of immutable objects, hashable
print(hash((None, True, False)))  # tuple of immutable objects, hashable
print(hash((b"bytes", bytes([1, 2, 3]))))  # tuple of immutable objects, hashable
print(hash((3 + 4j, 1 + 2j)))  # tuple of immutable objects, hashable
print(hash(range(5, 15)))  # range, hashable
print(hash("".join(["a", "b", "c"])))  # string, hashable
print(hash((1.1, 2.2, 3.3)))  # tuple of immutable objects, hashable

print(hash((1, 2, 3)))  # tuple of immutable objects, hashable
print(hash(frozenset([1, 2])))  # hashable

# x = hash(set([1,2])) #set unhashable
# x = hash(([1,2], [2,3])) #tuple of mutable objects, unhashable
# x = hash({1,2}) #list of mutable objects, unhashable
# x = hash([1,2,3]) #list of immutable objects, unhashable


# List of immutable types:

# int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

# List of mutable types:

# list, dict, set, bytearray, user-defined classes


# %%

# https://portal.mhhelpline.com/
# GlobalLogic*3*2025

# %%

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")
# %%


# %%
json_data = {
    "name": "John Doe",
    "age": 30}


