import collections

# namedtuple - when we want to make a tuple that is more readable and accesable but not too much like a class
import string

Point = collections.namedtuple("Point", ["x", "y"])
p1 = Point(10,20)
print(p1)  # Point(x=10, y=20)
p2 = Point(30,40)
print(p2)  # Point(x=30, y=40)
p1 = p1._replace(x=0)
print(p1.x)  # 0
print(p1._fields)  # ('x', 'y')
print(p1._asdict())  # {'x': 0, 'y': 20}
print(Point._make([5,5]))  # Point(x=5, y=5)

# defaultdict - have init value if key is not in dict
from collections import defaultdict
our_dict = defaultdict(int)
our_dict["new_key"] += 1  # init to 0 and then += 1
print(our_dict["new_key"])  # 1

our_dict = defaultdict(list)  # set our similar
our_dict["new_key"].append("first val")  # init to [] and then appends "first val"
print(our_dict["new_key"])  # ['first val']

our_dict = defaultdict(str)
our_dict["new_key"] += "a"  # init to "" and then appends "a"
print(our_dict["new_key"])  # a

our_dict = defaultdict(lambda: 100)  # start at 100
our_dict["new_key"] += 10  # init to "" and then appends "a"
print(our_dict["new_key"])  # 110


# OrderDict - maintain order of insertion
our_dict = collections.OrderedDict()
our_dict["first"] = 1
our_dict["second"] = 2
our_dict["third"] = 3
print(our_dict)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])
our_dict.popitem()  # can pop last element.
print(our_dict)  # OrderedDict([('first', 1), ('second', 2)])
our_dict.popitem(False)  # if we insert False than first item will be popped
print(our_dict)  # OrderedDict([('second', 2)])
print(our_dict == {"second": 2})  # True - Because when we try to compare with non order dict there is not importance
# for the order.


# deque - list with ability to pop and append from the start.
d = collections.deque(string.ascii_lowercase)
d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)  # deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
d.rotate(1)  # move the end to the right. equal to: val = d.pop(); d.appendleft(val)
print(d)  # deque([2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])
d.rotate(len(d))
print(d)  # deque([2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'])



