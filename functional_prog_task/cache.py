def cache(size= 10):
    def decorator(func):
        store = {}
        def inner(*args):
            if args in store:
                return store[args]
            else:
                if len(store) == size:
                    del store[next(iter(store))]
                result = func(*args)
                store[args] = result
                return result
        return inner
    return decorator


@cache(size= 5)
def math(x):
    return x * 2

@cache()
def add5(a):
    return a + 5

@cache()
def multiply5(a,b,c,d):
    return a * 5 + b+ c+ d

print(add5(2))
print(multiply5(2,3,4,5))

write_num = input('Num or stop')
while write_num != 'stop':
    print(math(int(write_num)))
    write_num = input()
