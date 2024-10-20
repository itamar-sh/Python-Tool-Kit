from typing import List


class Solution:
    """
    A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
    Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
    """
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        # left will be smaller than right each round
        # we will jump for next right if there is some greater right in the future.
        # This we can check by checking nums[left] > right_max[right] - which make right += 1 if nums[left] is small
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width