from heapq import heapify, heappush, heappop


# Heap is a binary tree which can be represent as an array
min_heap = []
heapify(min_heap)

# Adding items to the heap using heappush - each insertion is O(log(n))
vals = ["30", "50", "70", "20"]
for val in vals:
    heappush(min_heap, val)

# Min value:
print(f"Min Value: {min_heap[0]}")
print(f"All heap: {min_heap}")


