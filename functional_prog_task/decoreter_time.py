import time


def timeit(func):
    def inside(*args: tuple, **kwargs: dict):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return print(f'function {func.__name__} finished in {end - start}')
    return inside


@timeit
def math(a: int, b: int):
    return a ** b ** 6


math(9, 9)
