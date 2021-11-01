from functools import lru_cache

@lru_cache(10)
def dividing(x):
    return x / 2

print([dividing(i) for i in range(100)])

print(dividing.cache_info())