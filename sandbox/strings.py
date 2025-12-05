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

print(string_[::-1])  # fastest and cleanest method
print(
    "-".join(reversed(string_))
)  # readable, also join will ITERATE throuhg whole string


# weird recursion method....
def recursion_reverse(string_):
    if len(string_) == 0:
        return string_
    else:
        return string_[-1] + recursion_reverse(string_[:-1])


print(recursion_reverse(string_))

# ?>>??????D??DAW?DA?WD?
# why
lsls = "0123456789"
print(lsls[2::-2])


# sum([int(x) ** len(str(string_)) for x in str(string_)])


# python thinks in UNICODE, so it can use any language or emodzi

# but you can do "abc" * 
# abcabc

# spidersripts

# .decode .encode 
# for network package handling

