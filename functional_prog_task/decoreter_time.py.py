import time


def decorater(func):
    def inside(*args: tuple):
        start = time.time()
        func(*args)
        end = time.time()
        print(f'Function {func}: finished in {end - start}')
        return func(*args)
    return inside


@decorater
def math(a: int, b: int):
    return a ** b ** 5


math(9, 9)
