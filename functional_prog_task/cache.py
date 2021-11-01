store = {}
def cache(func):

    def inner(arg):
        if arg in store:
            print('found in cache')
            return store[arg]
        else:
            if len(store) == 10:
                del store[next(iter(store))]
            result = func(arg)
            store[arg] = result
            print(result,store)
            return func(arg)
    #print(store)
    return inner


@cache
def math(x):
    return x * 2

write_num = input('Num or stop')
while write_num != 'stop':
    print(math(int(write_num)))
    write_num = input()

