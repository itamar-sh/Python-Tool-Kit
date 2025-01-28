"""2762. Continuous Subarrays
Solved
Medium
Topics
Companies
Hint

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

    Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array."""

from sortedcontainers import SortedDict
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Use a SortedDict to maintain the sorted frequency map
        freq = SortedDict()
        left = right = 0
        count = 0  # Total count of valid subarrays

        while right < len(nums):
            # Add current element to frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while freq.peekitem(-1)[0] - freq.peekitem(0)[0] > 2:  # max(freq) - min(freq)
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Add count of all valid subarrays ending at right
            count += right - left + 1
            right += 1

        return count