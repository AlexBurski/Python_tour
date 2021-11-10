import time


def timeit(func):
    def inside(*args: tuple, **kwargs: dict):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'function {func.__name__} finished in {end - start}')
        return result
    return inside


@timeit
def math(a: int, b: int):
    return a * b


rv = math(1, 2)
assert rv == 2


print(math(9, 9))
