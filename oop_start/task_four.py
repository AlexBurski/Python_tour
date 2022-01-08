"""класс должен принимать два параметра
upper_limit и lower_limit (оба параметра не обязательные)
и реализовать метод is_valid """
from task_two_three import Metric


class CheckLimit(Metric):
    def __init__(self, value: int, unit: str, lower_limit: int = None, upper_limit: int = None):
        super().__init__(value, unit)
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def is_valid(self):
        if self.lower_limit:
            if self.upper_limit:
                return all((self._value < self.upper_limit, self._value > self.lower_limit))
            return self._value > self.lower_limit
        elif self.upper_limit:
            return self._value < self.upper_limit


b = CheckLimit(111, "hello", 112, 120)

print(b.is_valid())  #-->False
print(b.get_set)     #--> 111