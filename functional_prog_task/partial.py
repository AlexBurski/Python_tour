"""

A function that works as partial and curry

"""

def add_numbers(x: int, y: int):
    return x + y

def add_two(x):
    return add_numbers(x, 2)


#print(add_two(5))


def multi(a: int, d: int):
    def multi_2(b: int):
        def multi_3(c: int):
            return a * b * c * d
        return multi_3
    return multi_2


def double_multiplication (a,b,c):
    return multi(a,b)(c)(2)

print(double_multiplication(2,3,5))