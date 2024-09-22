# Typing
from typing import List
some_lst: List
# Declarations  - O(n)
lst = list()
lst2 = []
lst3 = list(lst2)  # any iterable
lst4 = list(set())
lst5 = [1, 2, 3, 4]
lst6 = [1, "2", lst3, set()]
lst7 = list(range(1, 10))  # [1,2,3,4,5,6,7,8,9]

# access  - O(1) for specific index, O(n) for slicing
a = lst6[3]
a2 = lst6[-2]
a3 = lst5[2:4]  # return new list [lst5[2], lst5[3]]  -  slicing
a4 = lst5[-3:-1]  # return new list [lst5[-3], lst5[-2]]  -  slicing
a5 = lst7[3:9:2]  # [4, 6, 8]
a6 = lst7[::2]  # [1, 3, 5, 7]
a7 = lst7[::-1]  # [9,8,7,6,..,1]  - backward

# change items
lst5[2] = 0
lst5[1:3] = [-1, -1]  # dangerous to insert in slicing more or less than the size of the slice.
lst6[1:2] = [-1, -1]  # will convert [1, "2", lst3, set()] to [1, -1, -1, lst3, set()] - "2" erased and the other moved
lst6[1:2] = []  # will convert [1, -1, -1, lst3, set()] to [1, -1, lst3, set()]
lst_old = [1]
lst_new = [2,3]
lst_new[:] = lst_old[:]  # insert all the elements in lst_old to lst_new without changing the pointer itself

# append and insert - adding elements
lst8 = [1, 2, 3, 4, 5]
lst.append(6)  # [1,2,3,4,5] -> [1,2,3,4,5,6]
lst5.insert(1, "inserted")  # [1,"inserted",2,3,4,5,6]  - O(n) operation

# remove items
lst9 = [1, 2, 3, 4, 5]
lst9.remove(3)  # [1, 2, 3, 4, 5] -> [1, 2, 4, 5]   # by value
val = lst9.pop(2)  # [1, 2, 5]   # by index - return lst9[2]  - raise error for false index
val2 = lst9.pop()  # [1, 2]   # by index - return lst9[-1]
del lst9[0]  # also remove, without return and raising errors
del lst9[:6]  # also remove by slicing

# sort
lst10 = [1,6,2]
lst10.sort()  # [1,2,6]
lst10.sort(reverse=True)  # [6,2,1]
lst10.sort(key= lambda a: a % 2)  # [2,6,1]

# copy lists
# if everything is primitive
lst11 = lst10[:]
lst12 = list(lst10)
lst13 = lst10.copy()
# if there is list inside list or another references
import copy
lst14 = copy.deepcopy(lst10)

# reverse the list
lst10.reverse()

# add new iterable in the and of the list
lst15 = [1, 2]
lst15.extend([3, 4, 5])  # [1,2,3,4,5]

# count(item) - count occurrences
print([1,2,3,4,3,1,12,3,4,3,2].count(2))  # 2


