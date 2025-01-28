from sortedcontainers import SortedList, SortedDict, SortedSet

# SortedList
sl = SortedList([10, 5, 2, 8])  # O(n*log(n))
sl.add(7)  # O(log(n))
sl.remove(5)  # O(log(n))
sl.discard(12) # O(log(n)) - don't raise error if not found
print("Element at index 1:", sl[1])
print("Is 10 in the list?", 10 in sl)
print("Index of 8:", sl.index(8))
print("Popped value:", sl.pop())
for value in sl:  # O(n)  - the values are sorted
    print("Iterating value:", value)
sl.clear()
sl.update([12, 3, 9])  # O(k*log(n))
new_sl = sl + SortedList([6, 11])
mult_sl = sl * 2  # multiply every value in the list
left_index = sl.bisect_left(7)  # Bisect left (finds insertion point for a value)
right_index = sl.bisect_right(7)  # Bisect right (insertion point to the right of equal values)
occurrences = sl.count(5)
range_values = sl.irange(3, 9)
sliced_values = sl.islice(1, 3)

max_val = sl.peekitem(-1)  # get max value - if SortedDict - then return pair (key, value)
min_val = sl.peekitem(0) # get min value