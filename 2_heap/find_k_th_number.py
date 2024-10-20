from heapq import heappop, heappush


def find_kth_largest_number(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # build min heap with size k, for k max values in nums
    min_heap = []  # O(1)
    for num in nums: # O(n)
        # Insert k first values
        if not min_heap or len(min_heap) < k:
            heappush(min_heap, num) # O(log(k))
        # Switch values if necessary
        elif num >= min_heap[0]:  # O(1) - get min on heap should be O(1)
            heappush(min_heap, num) # O(log(k))
            heappop(min_heap)  # O(log(k))
    return heappop(min_heap)