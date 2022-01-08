"""использую регулярки сделай проверку корректность ввода номера телефона"""

import re


def is_phone_num_valid(number: str, c_code: str = '375', op_code: str = '29'):
    REGEX = re.compile(fr'\+?(?P<country_c>{c_code})[ -]?(?P<oper_code>{op_code})[ -]?\d{{3}}[ -]?\d{{2}}[ -]?\d{{2}}')
    return bool(re.fullmatch(REGEX, number))


print(is_phone_num_valid("+37529 21452793"))  # False
print(is_phone_num_valid("+37529 2145793"))  # True
print(is_phone_num_valid("+35734 2126593"))  # False
print(is_phone_num_valid("37529 2oo5o63"))  # False
print(is_phone_num_valid("375-293145756"))  # True
print(is_phone_num_valid("375-33 31457-56", op_code='33'))  # True
