from typing import List
import random


class Median:
    @staticmethod
    def find_median_naive(nums: List[int]):
        """ Classic O(n*log(n)) solution. """
        nums.sort()
        if len(nums) % 2 == 0:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2)+1]) / 2


    @staticmethod
    def find_median_quickselect(nums: List[int]):
        """
        QuickSelect is Divide an Conquer solution. Originally to find the k-th number.
        It's worst case is O(n^2) but is average case is O(n).
        The algorithm picks randomely at each iteration a pivot number and partition the list who is before him and who is under.
        In best case the algorithm takes each time the middle number so the rest of the number to check are n/2 numbers.
        """
        def quickselect(arr, k):
            """
            This Solution is not optimized since it's create two extra arrays for every partition.
            But it's still O(len(arr)) for every paritition so it's ok.
            Quick Sort approach where you change the numbers location could work better.
            """
            if len(arr) == 1:
                return arr[0]

            pivot = random.choice(arr)
            lows = [el for el in arr if el < pivot]
            highs = [el for el in arr if el > pivot]
            pivots = [el for el in arr if el == pivot]

            if k < len(lows):
                return quickselect(lows, k)
            elif k < len(lows) + len(pivots):
                return pivots[0]
            else:  # k > len(lows+pivots)
                return quickselect(highs, k - len(lows) - len(pivots))

        n = len(nums)
        if n % 2 == 1:
            return quickselect(nums, n // 2)
        else:
            left_mid = quickselect(nums, (n // 2) - 1)
            right_mid = quickselect(nums, n // 2)
            return (left_mid + right_mid) / 2