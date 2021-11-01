from functools import partial


def addy(x: int, y: int):
    return x + y


new_func = partial(addy, y=2)


#print(new_func(5))


def multi(a: int, d: int):
    def multi_2(b: int):
        def multi_3(c: int):
            return a * b * c * d
        return multi_3
    return multi_2


multiplication = partial(multi, d=3)

print(multiplication(2)(3)(4))
