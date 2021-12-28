
"""Создать классMetric принимает аргументы value: int и unit: str
доступ к атрибутам value и unit нужно закрыть
и сделать get set через property unit должен быть только читаемым
на set для value нужно сделать валидацию что задачи интовое значение иначе делать ошибку ValueError"""
class Metric:
    def __init__(self, value: int, unit: str):
        self._value = value
        self._unit = unit

    @property
    def get_set(self):
        return self._value

    @get_set.setter
    def get_set(self, new_value: int):
        if isinstance(new_value, int):
            self._value = new_value
        else:
            raise ValueError("Must be an integer")

    @get_set.deleter
    def get_set(self):
        del self._value

if __name__ == "__main__":
    a = Metric(1, "abc")
    a.get_set = 125
    print(a.get_set) # 125
    del a.get_set
    print(a.get_set) # AttributeError:...