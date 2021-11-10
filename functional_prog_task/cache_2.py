def cache(size= 10):
    def decorator(func):
        store = {}
        def inner(*args, **kwargs):
            arg_comb = (args, tuple(kwargs.items()))
            if arg_comb in store:
                return store[arg_comb]
            else:
                if len(store) == size:
                    del store[next(iter(store))]
                result = func(*args, **kwargs)
                store[arg_comb] = result
                return result
        return inner
    return decorator

@cache()
def test_foo(a= 1,  b = 2):
    return a + b

#print(test_foo(a=10, b = 4))

#print(test_foo(),test_foo(3,4),test_foo(100,5),test_foo(3,4),test_foo( b = 2),test_foo(4),test_foo(), test_foo(a = 2))
