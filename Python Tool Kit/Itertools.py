import itertools

# cycle(iterable) - iterate in cycle over sequence
seq = [1,2,3]
cycle_seq = itertools.cycle(seq)
print(next(cycle_seq))  # 1
print(next(cycle_seq))  # 2
print(next(cycle_seq))  # 3
print(next(cycle_seq))  # 1


# count(start=0, step=0) - a counter
counter1 = itertools.count()
print(next(counter1))  # 0
print(next(counter1))  # 1
counter2 = itertools.count(5)
print(next(counter2))  # 5
print(next(counter2))  # 6
counter3 = itertools.count(5, 5)
print(next(counter3))  # 5
print(next(counter3))  # 10


# accumulate(iter, func=add)
vals = [1,2,3,4,5]
print(list(itertools.accumulate(vals)))  # [1, 3, 6, 10, 15]
print(list(itertools.accumulate(vals, max)))  # [1, 2, 3, 4, 5]
print(list(itertools.accumulate(vals, min)))  # [1, 1, 1, 1, 1]


# chain func will add two sequences together
print(list(itertools.chain([1,2,3], {4, 5, 2})))  # [1, 2, 3, 2, 4, 5]


# takewhile(condFunc, iterable), dropwhile(condFunc, iterable) - both take values from iterables.
# takewhile take until some condition is broken and dropwhile keep drop until condition is broken.
print(list(itertools.takewhile(lambda a: type(a) == int, [2,3,4,"not a number", 5, 6,7])))  # [2, 3, 4]
print(list(itertools.dropwhile(lambda a: type(a) == int, [2,3,4,"not a number", 5, 6,7])))  # ['not a number', 5, 6, 7]


# compress(iter, selector) - selector is some iterable with 0/False or 1/True to choose if we pick the value from iter.
print(list(itertools.compress([1,2,3,4,5], [0,1,1,1,0])))  # [2, 3, 4]
print(list(itertools.compress([1,2,3,4,5], itertools.cycle([0,1]))))  # [2, 4]


# product(*iterables, repeat=1) - do Cartesian product of input iterables.
print(list(itertools.product("ABCD", repeat=2)))  # 4**2
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'),
# ('C', 'B'), ('C', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]
print(list(itertools.product("ABCD", repeat=3)))  # 4**3 - AAA,AAB,AAC,AAD,ABA,ABB,..,DDD
print(list(itertools.product("AB", "CD")))  # 2*2=4
# [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]


# permutations(iterable, permutation_len) - all permutations with permutation_len from iterable
# permutations are values from the iter with specific order.
# it's like product without repeat
print(list(itertools.permutations("ABCD", 2)))  # 4*3
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'),
# ('D', 'A'), ('D', 'B'), ('D', 'C')]
print(list(itertools.permutations("ABCD", 3)))  # 4*3*2 = 24
# [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'),
# ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'),
# ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'),
# ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
print(list(itertools.permutations("AABC", 2)))  # 4*3 - no difference between two A's
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'A'), ('B', 'C'),
# ('C', 'A'), ('C', 'A'), ('C', 'B')]
print(list(itertools.permutations("AB", 5)))  # no enough values for ordering of 5 items.
# []


# combinations(iterable, combination_len) - all combinations with combination_len from iterable - without replacement
# combinations are values from the iter. No importance of the order.
# no replacement mean's that each occurrence in the iterable will appear only once.
# O(n**k) - while n is iter length and k is combination_len and k is fixed.
print(list(itertools.combinations("ABCD", 2)))  # 2 choose 4: 6 combs
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
print(list(itertools.combinations("ABCD", 3)))  # 3 choose 4: 4 combs
# [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
print(list(itertools.combinations("AABC", 2)))  # (2 choose 3) + 1: 5 combs
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.combinations("AB", 5)))  # no enough values. This is the meaning of replacement
# []

# combinations_with_replacement(iterable, combination_len) -
# all combinations with combination_len from iterable - with replacement
# combinations are values from the iter. No importance of the order.
# replacement mean's that each occurrence in the iterable can appear many times.
# O(n**k) - while n is iter length and k is combination_len and k is fixed.
print(list(itertools.combinations_with_replacement("ABCD", 2)))  # 4+3+2+1 = 10
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]
print(list(itertools.combinations_with_replacement("ABCD", 3)))  # 4+3+2+1 + 3+2+1 + 2+1 + 1 = 19
# [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'A', 'D'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'B', 'D')
# , ('A', 'C', 'C'), ('A', 'C', 'D'), ('A', 'D', 'D'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'B', 'D'), ('B', 'C', 'C'),
# ('B', 'C', 'D'), ('B', 'D', 'D'), ('C', 'C', 'C'), ('C', 'C', 'D'), ('C', 'D', 'D'), ('D', 'D', 'D')]
print(list(itertools.combinations_with_replacement("AABC", 2)))  # 4+3+2+1 = 10
# [('A', 'A'), ('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(list(itertools.combinations_with_replacement("AB", 5)))  # 6
# [('A', 'A', 'A', 'A', 'A'), ('A', 'A', 'A', 'A', 'B'), ('A', 'A', 'A', 'B', 'B'), ('A', 'A', 'B', 'B', 'B'),
# ('A', 'B', 'B', 'B', 'B'), ('B', 'B', 'B', 'B', 'B')]






