"""класс должен принимать два параметра
upper_limit и lower_limit (оба параметра не обязательные)
и реализовать метод is_valid """

from task_two_three_metric import Metric


class Check_limit(Metric):
    def __init__(self, value: int, unit: str):
        super().__init__(value, unit)

    def is_valid(self, lower_limit=0, upper_limit=999):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        return all((self._value < self.upper_limit, self._value > self.lower_limit))


b = Check_limit(111, "hello")

print(b.is_valid(0, 100)) #-->False
print(b.get_set)    #--> 111
