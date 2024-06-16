class SearchInt:

    def two_sum(self, nums, num_target):
        """
        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.
        """
        # Note - if there is a duplicate number we will insert only one.
        indices_dict = dict()
        for index, num in enumerate(nums):
            if num_target-num in indices_dict:
                return indices_dict[num_target-num], index
            else:
                indices_dict[num] = index

    def two_sum_with_sort_and_enum(self, nums, num_target):
        """
        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.
        """
        sorted_nums_with_index = sorted(enumerate(nums), key=lambda num_tuple: num_tuple[1])
        left = 0
        right = len(sorted_nums_with_index) - 1

        while left < right:
            result = sorted_nums_with_index[left][1] + sorted_nums_with_index[right][1]
            if result == num_target:
                return sorted_nums_with_index[left][0], sorted_nums_with_index[right][0]
            elif result > num_target:
                right -= 1
            else:
                left += 1

    def find_median_of_two_sorted_array(self, nums1, nums2):
        """
        Problem:
        Given two sorted arrays nums1 and nums2 of size m and n respectively,
        return the median of the two sorted arrays.
        The overall run time complexity is O(min(log (m), log(n)).
        Solution:
        Binary Search on the short array, each time the median index of the
        long array is determined by the the position of the short array.

        The right partition is catched in case the values of one cell left to
        the value of the cell of the mid index of the short array is smaller
        than the value of the cell of the index of the long array and vice versa.

        Calculation of the result depends if the total size of the arrays is
        odd or even, we take max and min of the results. (Should reconsider why)
        """
        if len(nums1) < len(nums2):
            short_array = nums1
            long_array = nums2
        else:
            short_array = nums2
            long_array = nums1

        short_array_size = len(short_array)
        long_array_size = len(long_array)
        total_arrays_size = short_array_size + long_array_size
        start_index = 0
        end_index = short_array_size

        while start_index <= end_index:
            short_mid_index = (start_index + end_index) // 2
            long_mid_index = ((total_arrays_size + 1) // 2) - short_mid_index

            # find values where the mid indices are on
            value_left_of_short_mid_index = short_array[short_mid_index - 1] if (short_mid_index - 1) >= 0  else float('-inf')
            value_of_short_mid_index = short_array[short_mid_index] if short_mid_index < short_array_size  else float('inf')
            value_left_of_long_mid_index = long_array[long_mid_index - 1] if (long_mid_index - 1) >= 0  else float('-inf')
            value_of_long_mid_index = long_array[long_mid_index] if long_mid_index < long_array_size  else float('inf')
            if value_left_of_short_mid_index <= value_of_long_mid_index and value_left_of_long_mid_index <= value_of_short_mid_index:
                # we found the solution
                if total_arrays_size % 2 == 1:
                    return max(value_left_of_short_mid_index, value_left_of_long_mid_index)
                else:
                    return (max(value_left_of_short_mid_index, value_left_of_long_mid_index) + \
                            min(value_of_long_mid_index, value_of_short_mid_index)) / 2.0
            elif value_left_of_short_mid_index > value_of_long_mid_index:
                end_index = short_mid_index - 1
            else:
                start_index = short_mid_index + 1
        raise ValueError("The input arrays are not sorted")
