from typing import Set, Dict

s: Set = set()
d: Dict = dict()
d2 = {}
# len
print(len(s)) # 0
len(d)
# add item
s.add("new item")
d["new item"] = 1
# access
for val in s:
    pass
for val in d:  # on keys
    pass
# not lists
print(d.keys())  # ["new item"]
print(d.values())  # [1]
print(d.items())  # [('new item', 1)]
# add iterables
s.update({"new item2": 1})
print(s)  # {'new item', 'new item2'}
# remove
s.remove("new item")  # will raise error if element does not exist
s.discard("new item")  # will not raise error if element does not exist
s.pop()  # return some element
# union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# intersect - Return a set that contains the items that exist in both set x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)  # {'apple'}

# difference - Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)  # {'cherry', 'banana'}

# isdisjoint() - Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)  # True

# issubset() - Return True if all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)  # True

# issuperset() Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)  # True

# update for dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year2": 2020})   # will not raise error if value is not there!
print(thisdict)
# remove item
thisdict.pop("model")
del thisdict["brand"]  # will raise error if "brand" not exist

# Do value += 1 if key exist else make a key with 1
new_dict = {}
key = "a"
new_dict[key] = new_dict.setdefault(key, 0) + 1
print(new_dict[key])  # 1
new_dict[key] = new_dict.setdefault(key, 0) + 1
print(new_dict[key])  # 2