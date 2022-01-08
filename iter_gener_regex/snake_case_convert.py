"""используя регулярки сделать функцию для конвертации строки в snake_case"""

import re


def convert_to_snake_case(string: str):
    result = re.sub("^\s*", '', string)
    result = re.sub("\s*$", '', result)
    result = re.sub("\s+", '_', result.lower())
    return result


print(convert_to_snake_case("   Hello   world    "))  # hello_world
