def non_stable_positive_numeric_counting_sort(nums, max_value):
    frequencies = [0 for _ in range(max_value+1)]
    for num in nums:
        frequencies[num] += 1
    f_index = 0
    for n_index in range(len(nums)):
        while frequencies[f_index] == 0:
            f_index += 1
        nums[n_index] = f_index
        frequencies[f_index] -= 1
    return nums


def stable_positive_numeric_counting_sort(nums, max_value):
    # 1) create frequencies array
    frequencies = [0 for _ in range(max_value+1)]
    for num in nums:
        frequencies[num] += 1
    # 2) convert frequencies array to cumulative counts of elements
    for f_index in range(1, len(frequencies)):
        frequencies[f_index] += frequencies[f_index-1]
    print(frequencies)
    # 3) place every element in result position - using cumulative counts of elements
    result = [-1 for _ in range(len(nums))]
    for num_index in range(len(nums)-1, -1, -1):
        num = nums[num_index]
        # frequencies[num] holds the final location of the last element in result
        result[frequencies[num]-1] = num
        frequencies[num] -= 1
    return result



def test_non_stable_positive_numeric_counting_sort():
    nums = [1,4,5,2,3,2,3,4,5,2]
    res = non_stable_positive_numeric_counting_sort(nums, 5)
    print(res)

def test_stable_positive_numeric_counting_sort():
    nums = [1,4,5,2,3,2,3,4,5,2]
    res = stable_positive_numeric_counting_sort(nums, 5)
    print(res)


