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