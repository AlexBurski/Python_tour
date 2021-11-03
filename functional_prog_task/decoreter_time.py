import time


def decorater(func):
    def inside(*args: tuple, **kwargs: tuple):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'finished in ', end - start)
        return func(*args, **kwargs)
    return inside


@decorater
def math(a: int, b: int):
    return a ** b ** 6


math(9, 9)
