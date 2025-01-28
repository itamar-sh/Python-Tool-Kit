"""2779. Maximum Beauty of an Array After Applying Operation

You are given a 0-indexed array nums and a non-negative integer k.

In one operation, you can do the following:

    Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
    Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + k].

The beauty of the array is the length of the longest subsequence consisting of equal elements.

Return the maximum possible beauty of the array nums after applying the operation any number of times.

Note that you can apply the operation to each index only once.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.
"""


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        max_val = max(nums)+1
        lines = [0] * (max_val)
        for num in nums:
            lines[max(0, num-k)] += 1
            if num+k+1 < max_val:
                lines[num+k+1] -= 1
        max_result = 0
        cur_res = 0
        for res in lines:
            cur_res += res
            max_result = max(cur_res, max_result)
        return max_result