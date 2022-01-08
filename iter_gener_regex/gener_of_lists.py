"""Реализовать генератор который принимает любое количество списков и при
итерации возвращает все элементы из этих списков по очереди
типо так for i in arr_iter(arr1, arr2, arr3)"""


def generator_of_lists(*args):
    for each_list in args:
        yield from each_list




g = generator_of_lists([1, 2, 4], ['a', 'b'], ['23', 52, 'Alex'])
print(g)  # <generator object generator_of_lists at 0x7f4d5aacc4c0>
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 4
print(next(g))  # a
print(next(g))  # b
print(next(g))  # 23
print(next(g))  # 52
print(next(g))  # Alex
print(next(g))  # StopIteration
