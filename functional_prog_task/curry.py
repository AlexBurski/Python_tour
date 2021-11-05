def hello(name: str):
    def howdy(statement: str):
        print(f'hello, dear {name}. I am extremely glad to see you and say that {statement}')
    return howdy

hello('Semyon')('you look great')

def adding(a: int):
    def adding_again(b: int):
        def double(c: int):
            return print((a + b + c) * 2)
        return double
    return adding_again

adding(1)(2)(3)

def add_numbers(a: int):
    def add_second(b: int):
        def last_add(c: int):
            return a+ b+ c
        return last_add
    return add_second


curry_plus_two = add_numbers(2)
curry_plus_three = curry_plus_two(3)

#print(curry_plus_three(5))

def multi(a):
    return lambda b,c: a*b*c

curry_double = multi(2)

#print(curry_double(3,4))