# * can use to dereference a list or to make something optional big
def flexFunc(*args):
    print(args[0], args[-1])

flexFunc(3,5,set(),8,[3,4,6], "ab")  # 3 ab

flexFunc(3,5,set(),8,[3,4,6])  # 3 [3, 4, 6]

# put attention to the dereference
flexFunc(3,5,set(),8, *[3,4,6])  # 3 6

# ** is for dictionaries: kwargs are: "key value args"

# def flex2Func(*args, **kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# flex2Func(**{"1":1, "2":2})



