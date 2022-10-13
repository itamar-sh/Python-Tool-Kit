# declare and defined
s: str
s = "a"
s = 'a'
s = """
a"""
# slicing
s = "123456789"
a = s[:]  # all
a2 = s[2:5]  # classic
a3 = s[-5:-2]  # regular
a4 = s[::-1]  # backward
a5 = s[::2]  # even
a6 = s[1::2]  # odd

# change to be upper and lower
s2 = " ab cdE3 "
s2 = s2.upper()  # "ABCDE3"
s2 = s2.lower()  # "abcde3
# remove whitespace from start and end
s2 = s2.strip()
# remove something else from the start
s3 = "ababcdab"
s3 = s3.strip("ab")  # "cd
# concatenate
s4 = s3 + " " + s2
# endwith() - returns True if the string ends with the specified value, otherwise False.
txt = "Hello, welcome to my world."

x = txt.endswith("my world.")  # True
# center() - method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x2 = txt.center(20)  #         banana
txt = "banana"
x3 = txt.center(20, "O")  #OOOOOOObananaOOOOOOO
# find() - finds the first occurrence of the specified value. returns -1 if the value is not found
txt = "Hello, welcome to my world."
x4 = txt.find("e")  # 1
x5 = txt.index("e")  # 1
x6 = txt.find("e", 5, 10)
x7 = txt.index("e", 5, 10)  # ValueError: substring not found
# islnum() - returns True if all the characters are alphanumeric: numbers and not space and !#%&? and etc
x8 = txt.isalnum()
# istitle() - Check if each word start with an upper case letter:
txt = "Hello, And Welcome To My World!"
x9 = txt.istitle()
# isupper() - returns True if all the characters are in upper case, otherwise False.
txt = "THIS IS NOW!"  # Numbers, symbols and spaces are not checked, only alphabet characters.
x10 = txt.isupper()
# isalpha(), isdigit(), islower() - understood
txt = "A"
x11 = txt.isalpha()  # True
x12 = txt.isdigit()  # False
x13 = txt.islower()  # False
# partition() - Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x14 = txt.partition("bananas")  # ('I could eat ','bananas',' all day')
# rpartition() - from the right
# rindex(), rfind() - first index from the right
x15 = "I could eat bananas all day".rpartition("bananas")  # ('I could eat ','bananas',' all day')
x16 = "I could eat bananas all day".rfind("bananas")  # 12
# split() Split a string into a list where each word is a list item
# string.split(separator, maxsplit) - optional args
x17 = "I could eat bananas all day".split()  # ["I","Could",...,"day"]
x18 = "I#could#eat#bananas#all#day".split(sep="#")  # ["I","Could",...,"day"]
x19 = "I could eat bananas all day".split(maxsplit=3)  # ["I","Could","eat bananas all day"]
# splitlines()  - each line is an element
txt = "Thank you for the music\nWelcome to the jungle"
x20 = txt.splitlines()  # ["Thank you for the music","Welcome to the jungle"]
# title() - Make the first letter in each word upper case:
txt = "Welcome to my world"
x21 = txt.title() # "Welcome To My World"
# join() - concatenating strings
x22 = "#".join(["a", "b", "c"])  # "a#b#c"
# replace() - replaces a specified phrase with another specified phrase.
# string.replace(oldvalue, newvalue, count)  # count is optional
txt = "I like bananas"
x23 = txt.replace("bananas", "apples")  # "I like apples"
x24 = "I like bananas bananas".replace("bananas", "apples", 1)  # "I like apples bananas"

# The maketrans() method returns a mapping table that can be used with the:
# translate() method to replace specified characters.
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")  # dict in unicode
print(mytable)  # {83: 80}

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)  # x, y same length
print(mytable)  # {109: 101, 83: 74, 97: 111}
print(txt.translate(mytable))  # "Hi Joe!"

# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(mytable)  # {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mytable))  # G i Joe!
print(mytable.values())  # dict_values([101, 74, 111, None, None, None, None, None, None])

# sort string
word = "34543dssdsd34"
sortedWord = ''.join(sorted(word))  # return str
print(sortedWord)  # 3334445dddsss
print(sorted(word))  # ['3', '3', '3', '4', '4', '4', '5', 'd', 'd', 'd', 's', 's', 's']

# count(substring, start=...,(Optional) end=...(Optional)) - how many occurrences of substring is a string
print("34343444444".count("34"))  # 3
