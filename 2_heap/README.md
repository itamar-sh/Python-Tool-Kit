# HEAP
Heap is the modern way to say "Priority Queue".
It's support getting the min/max at O(1).
Insert/Delete/Update value in O(log(n)).

We can use him as min_heap in the heapq module.
` from heapq import heappush, heappop `

Building heap is O(n) - which is efficient.
But inserting list of elements one by one will take O(n*log(n)).

# TO DO
Implement build_max_heap, heapsort, heap_increase_key, heap_insert.
Also using heapq for max_heap using insert every value as his minus.