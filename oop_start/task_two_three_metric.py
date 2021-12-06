"""Создать классMetric принимает аргументы value: int и unit: str
доступ к атрибутам value и unit нужно закрыть
и сделать get set через property unit должен быть только читаемым

на set для value нужно сделать валидацию что задачи интовое значение иначе делать ошибку ValueError"""


class Metric:
    def __init__(self, value: int, unit: str):
        self._value = value
        self.__unit = unit

    @property
    def get_set(self):
        if isinstance(self._value, int):
            return self._value
        raise ValueError("Must be an integer")




