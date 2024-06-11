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
        pass