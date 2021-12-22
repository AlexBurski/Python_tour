"""Реализовать итератор infinite(arr, repeat)
arr - список
repeat - число сколь раз повторить
и сделать так что бы при итерации по нем через for проход по arr повторялся заданое количество(repeat) раз"""


class RepeatedIterator:
    def __init__(self, arr: list, repeat: int):
        self.arr = arr
        self.repeat = repeat
        self.wider_arr = self.arr * self.repeat
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.wider_arr):
            raise StopIteration
        element = self.wider_arr[self.index]
        self.index += 1
        return element


g = RepeatedIterator([1, 4, 7, "Alesha", "44"], 3)

for el in g:
    print(el, end=' ')  # 1 4 7 Alesha 44 1 4 7 Alesha 44 1 4 7 Alesha 44
