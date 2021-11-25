# create a csv-file with 300 random strings

import csv
import random
from random_word import RandomWords


def make_csv_file():
    new_file = open('file.csv', 'w', encoding='utf-8', newline='')
    file_writer = csv.writer(new_file)
    head = ['ID', 'first_name', 'last_name', 'age']
    file_writer.writerow(head)
    first_name = RandomWords().get_random_words(limit=300)
    last_name = RandomWords().get_random_words(limit=300)
    for i in range(300):
        file_writer.writerow([random.randint(1, 300), random.choice(first_name), random.choice(last_name), random.randint(10, 90)])
    new_file.close()
