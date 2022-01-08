"""у тебя есть масив названий файлов такого вида
0001_is32fjf32.py
тебе нужно используя регулярки найти максимальное число с которого начинается название файла"""

import re


def find_the_largest_name(list_of_names: list):
    used_numbers = []
    num_compiler = re.compile('(?P<clean_number>\d+)_')
    for name in list_of_names:
        number = re.search(num_compiler, name)
        used_numbers.append(int(number.group("clean_number")))
    return max(used_numbers)


print(find_the_largest_name(["0001_01f60e6ec6a4.py",
                             "0102_9e21743de53d.py",
                             "0003_0054440550a5.py",
                             "0004_f45301d9b8b8.py", ]))  # 102
