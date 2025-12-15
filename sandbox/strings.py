# strings are immutable
# each concatenation, slice or adding new words to string
# create new object

# we can use [:] or slice()

string_ = "Revert me please:)"


# While loop is less efficient
def method_1():
    answer = ""
    i = len(string_) - 1
    while i >= 0:
        answer += string_[i]
        i -= 1
    return answer


# for loops is slower due to immutability
def method_2():
    answer = ""
    for letter in string_:
        answer = letter + answer
    return answer


def method_3():
    answer = ""
    letters = []
    for letter in string_:
        letters.append(letter)
    return answer.join(reversed(letters))


# print("\n" + method_1() + "\n" + method_2() + "\n" + method_3())

# other (smarter) solutions

# print(string_[::-1])  # fastest and cleanest method
print(
    # "-".join(reversed(string_))
)  # readable, also join will ITERATE throuhg whole string


# weird recursion method....
def recursion_reverse(string_):
    if len(string_) == 0:
        return string_
    else:
        return string_[-1] + recursion_reverse(string_[:-1])


# print(recursion_reverse(string_))

# ?>>??????D??DAW?DA?WD?
# why
lsls = "0123456789"
# print(lsls[2::-2])


# sum([int(x) ** len(str(string_)) for x in str(string_)])


# python thinks in UNICODE, so it can use any language or emodzi

# but you can do "abc" * 
# abcabc

# spidersripts

# .decode .encode 
# for network package handling


tests = [([1,2,3,4,5], [2,3,4,5]), ([5,4,1,3], [5,4,3]), ([1,2,1], [2,1])]

def remove_smallest(list_):
    newlist = list_.copy()
    newlist.remove(min(list_))
    return newlist

def loop():
    for test in tests:
        print(test[0], test[1])    
        result = remove_smallest(test[0])
        assert result == test[1], "Wrong :("
        assert result is not test[0], "You can't change original list"

loop()


def test_me(x=333, y=7553):
    res = []
    for i in range(x,y+1):
        if i % 7 == 0  and i % 13 == 0 and i % 5 != 0:
            res.append(i)
    return res

print(test_me())

test_strings = ["kawabunga", "metro2013", "moon", "orange"]

# def shwalengthimeter(test_strings):
#     ans = []
#     vowels = "aeiouAEIOU"
#     for string in test_strings:
#         ans.append(f"shwa{string[2:]} {len(string)}") if string[1] in vowels else ans.append(f"shwa{string[1:]} {len(string)}")
#     return ans

def shwalengthimeter(test_strings):
   return [f"shwa{string[2:]} {len(string)}" if string[1] in "aeiou" else f"shwa{string[1:]} {len(string)}" for string in test_strings]

print(shwalengthimeter(test_strings))


