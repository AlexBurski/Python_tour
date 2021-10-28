from functools import lru_cache 

@lru_cache(10)
def dividing(x: int):
    return x / 2