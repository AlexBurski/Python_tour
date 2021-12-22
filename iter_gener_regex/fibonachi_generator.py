"""Реализовать генератор возвращающий числа фибоначи fib(n) до n'нного числа"""


def gen_fibonachi(n: int):
    if n <= 0:
        raise ValueError
    a, b = 1, 0
    for num in range(n):
        yield b
        a, b = b, a + b


g = gen_fibonachi(10)
print(g)  # <generator object gen_fibonachi at 0x7feaf04a94c0>
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 5
print(next(g))  # 8
print(next(g))  # 13
print(next(g))  # 21
print(next(g))  # 34
print(next(g))  # StopIteration
