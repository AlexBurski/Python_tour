"""
Function compose that takes infinite num of function and call then all
"""

from functools import reduce


# a = lambda x: x + 1
# b = lambda x: x + 3
# c = lambda x: x - 3
# d = lambda x: x - 1


def compose(*func: tuple):
    def compose2(func1, func2):
        return lambda x: func1(func2(x))

    return reduce(compose2, func)

# f = compose(a, b, c, d)

# print(f(4)) 