# cook your dish here


# nums = [8, 2, 14, 18, 100000]
# results = []

# def get_most_two(num):
#     two = 2
#     while num > two:
#         two *= 2
#     print("num, two", num, two)
#     return two

# for num_index in range(len(nums)):
#     num = nums[num_index]
#     two_above = get_most_two(num)
#     results.append(num - (two_above-num) if num != two_above else 0)
# for result in results:
#     print(result)
    
# ##########################################################3

# def find_min(arr):
#     cur_bit_value = 1
#     combined_or = 0
#     original_size = len(arr)
#     old_arr = arr
#     arr = dict()
#     for num in old_arr:
#         if num in arr:
#             arr[num] += 1
#         else:
#             arr[num] = 1
#     for num in arr:
#         combined_or = combined_or | num
#     while cur_bit_value < combined_or:
#         if cur_bit_value & combined_or != cur_bit_value:
#             value_to_remove = []
#             for num in arr:
#                 if num > cur_bit_value:
#                     value_to_remove.append(num)
#             for num in value_to_remove:
#                 del arr[num]
#             combined_or = 0
#             for num in arr:
#                 combined_or = combined_or | num
#             cur_bit_value = 1
#         else:
#             cur_bit_value = cur_bit_value << 1
#     print(original_size-sum(arr.values()))


# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     find_min(A)


############################################3

# cook your dish here
def find_next_two_primes(x):
    n = max(x+10, x*2)
    is_prime = [True] * (n+1)
    p = 2
    primes = []
    while (p * p) <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p += 1
    for num in range(x, n):
        if num > 1 and is_prime[num]:
            primes.append(num)
        if len(primes) == 2:
            break
    print(primes[0] * primes[1])


T = int(input())
for test_case in range(T):
    x = int(input())
    find_next_two_primes(x)