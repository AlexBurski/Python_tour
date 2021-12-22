"""использую регулярки сделай проверку корректность ввода номера телефона"""

import re


def is_phone_num_valid(number: str, country_code: str = '375', operator_code: str = '29'):
    REGEX = re.compile(fr'\+?{country_code}{operator_code}\s?\d{{7}}')
    return bool(re.fullmatch(REGEX, number))


print(is_phone_num_valid("+37529 21452793"))  # False
print(is_phone_num_valid("+37529 2145793"))  # True
print(is_phone_num_valid("+35734 2126593"))  # False
print(is_phone_num_valid("37529 2oo5o63"))  # False
print(is_phone_num_valid("375293145756"))  # True
