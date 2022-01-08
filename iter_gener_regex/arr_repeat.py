"""Реализовать итератор infinite(arr, repeat)
arr - список
repeat - число сколь раз повторить
и сделать так что бы при итерации по нем через for проход по arr повторялся заданое количество(repeat) раз"""


class RepeatedIterator:
    def __init__(self, arr: list, repeat: int):
        self.arr = arr
        self.repeat = repeat
        self.index = 0
        self.repeated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.arr):
            self.index = 0
            self.repeated += 1
            if self.repeated >= self.repeat:
                raise StopIteration
        element = self.arr[self.index]
        self.index += 1
        return element


g = RepeatedIterator([1, 4, 7, "Alesha", "44"], 3)

for el in g:
    print(el, end=' ')  # 1 4 7 Alesha 44 1 4 7 Alesha 44 1 4 7 Alesha 44


class RepeatedGenerator(RepeatedIterator):
    def __init__(self, arr: list, repeat: int):
        super().__init__(arr, repeat)
        self.wider_arr = (x for _ in range(self.repeat) for x in self.arr)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.wider_arr)
