import re

"""
1) re.search(regex: str, word: str) - search the regex in word
^The - check if word start in "The.
Spain$ - check if word ends with "Spain"
.* - check if there is zero or more occurrences of "." which represents anything
"""
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # Returns a Match object if there is a match anywhere in the string
print(x)  # <re.Match object; span=(0, 17), match='The rain in Spain'>
print(x.string)  # The rain in Spain
print(x.span())  # (0, 17)
print(x.start())  # 0
print(x.end())  # 17
print(x.regs)  # ((0, 17),)
print(x.group())  # The rain in Spain
"""
2) search return None if no match has found
\s - chcck for space
3) find all return list of all occurrences
"""
print(re.search("\s", "no_space_here"))  # None
print(re.search("\s", "two space here").span())  # (3, 4) return first span of regex
print(re.findall("\s", "two space here"))  # [' ', ' ']
print(re.findall("ai", "The rain in Spain"))  # ['ai', 'ai']
print(re.findall(".*", "The rain in Spain"))  # ['The rain in Spain', '']
print(re.findall("T.*", "The The"))  # ['The The']
print(re.findall("T.*he", "The The"))  # ['The The']
"""
4) sub(regex, replacement, word, max_replace[Optional]) - replace word
"""
print(re.sub("\s", "9", "The rain in Spain"))  # The9rain9in9Spain
